"""
API client for the Locksmith KDM service
"""

import os
import os.path
import urllib
import urllib2
import json
import fnmatch
import re

LOCKSMITH_HOST = 'https://locksmith.artsalliancemedia.com'

def setup_auth(uri, username, passwd):
    """
    Set the basic auth handler for all calls
    """
    passwd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passwd_mgr.add_password(None, uri, username, passwd)
    handler = urllib2.HTTPBasicAuthHandler(passwd_mgr)
    return urllib2.build_opener(handler)


class AuthorisationError(Exception):
    """
    Authentication failure with Locksmith
    """
    pass


class Lockpyck(object):
    """
    Locksmith wrapper class for encapsulating communication with
    the Locksmith service
    """

    def __init__(self, username, passwd, host=LOCKSMITH_HOST):
        self._host = host
        self._username = username
        self._passwd = passwd
        self.url_opener = setup_auth(host, self._username, self._passwd)
    
    @property
    def version(self):
        """
        Returns the Locksmith service's current version
        """
        response = self.url_opener.open(self._host + '/api')
        if response.code == 200:
            return json.loads(response.read())['version']

    def kdm(self, kdm_uuid):
        """
        Returns a dictionary of a KDM and its metadata from a UUID.
        If no KDM is found, then an empty dictionary is returned.
        """
        response = self.url_opener.open(self._host + '/api/kdm/id/' + kdm_uuid)
        if response.code == 200:
            return json.loads(response.read())

    def kdms_from_thumbprint(self, thumbprint):
        """
        Returns a list of KDM dictionaries who are both not expired and match to the
        given thumbprint
        """
        response = self.url_opener.open(self._host + '/api/kdm/thumbprint/' + thumbprint)
        if response.code == 200:
            return json.loads(response.read())

    def kdm_bundle(self, cpl_uuid, thumbprint, save_path=None):
	"""
	Retrieves a KDM bundle for the specified CPL and server thumbprint
	and saves it to the specified location if one is specified, otherwise
	return the filename and tar data as a tuple
	"""
        response = self.url_opener.open(self._host + '/api/tkr/' + cpl_uuid + '/' + thumbprint)
	if response.code == 200:
	    # Get the filename from the HTML headers
	    p = re.compile('attachment; filename="(.*)"')
	    filename = p.match(response.info().getheader('Content-Disposition')).group(1)
	    if save_path:
	        with open(os.path.join(save_path, filename), 'w') as f:
	            f.write(response.read())
	    else:
		return (filename, response.read())

    def save_kdm(self, kdm_xml):
        """
        Uploads a KDM to Locksmith
        """
        data = urllib.urlencode({'kdm' : kdm_xml})
        response = self.url_opener.open(self._host + '/api/kdm/save/', data)
        if response.code == 200:
            return json.loads(response.read())

    def batch_load_kdms(self, kdm_dir):
        """
        Loads all KDMs that the system can recursively find in the specified directory
        """
        count = 0
        for root, dirs, files in os.walk(kdm_dir):
            for filename in fnmatch.filter(files, '*.xml'):
                print 'Saving %s' % os.path.join(root, filename)
                count += 1
                print 'Count: %d' % count
                with open(os.path.join(root, filename), 'r') as f:
                    self.save_kdm(f.read())
