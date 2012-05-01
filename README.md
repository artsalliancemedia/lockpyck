Lockpyck
========

A client library for accessing the [Locksmith KDM service](http://locksmith.artsalliancemedia.com).

Usage
-----

```python
from lockpyck import Lockpyck

lockpick = Lockpick('user', 'password')
    print lockpick.version
    print len(lockpick.get_kdms_from_thumbprint('98a48a64c18f8e7f5df4c4036a188c1e5a8f59e4'))
    lockpick.batch_load_kdms('/some/dir/')
