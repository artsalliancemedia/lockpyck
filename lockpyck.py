"""
API client for the Locksmith KDM service
"""

import os
import urllib
import urllib2
import json
import fnmatch

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


class Lockpick(object):
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

    def get_kdm(self, kdm_uuid):
        """
        Returns a dictionary of a KDM and its metadata from a UUID.
        If no KDM is found, then an empty dictionary is returned.
        """
        response = self.url_opener.open(self._host + '/api/kdm/id/' + kdm_uuid)
        if response.code == 200:
            return json.loads(response.read())

    def save_kdm(self, kdm_xml):
        """
        Uploads a KDM to Locksmith
        """
        data = urllib.urlencode({'kdm' : kdm_xml})
        response = self.url_opener.open(self._host + '/api/kdm/save/', data)
        if response.code == 200:
            return json.loads(response.read())

    def get_kdms_from_thumbprint(self, thumbprint):
        """
        Returns a list of KDM dictionaries who are both not expired and match to the
        given thumbprint
        """
        response = self.url_opener.open(self._host + '/api/kdm/thumbprint/' + thumbprint)
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
