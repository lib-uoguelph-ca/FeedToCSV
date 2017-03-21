# FeedToCSV

# Archive.org Import

## Python internet archive module
* https://github.com/jjjake/internetarchive
* https://internetarchive.readthedocs.io/en/latest/

## Sessions
Some functionality requires an active session. Sessions are loaded from a config file.
You can create the config file like so:
```
from internetarchive import configure
configure('user@example.com', 'password', config_file='ia.ini')
```

Once you've done that, load your session data:

```
from internetarchive import get_session
s = get_session(config_file='ia.ini')
```

## Search
You can use ia search to create an itemlist, scoped to a collection:

`$ ia search 'collection:glasgowschoolofart' --itemlist > itemlist.txt`

API interface - See: https://internetarchive.readthedocs.io/en/latest/api.html#searching-items

## File download
https://internetarchive.readthedocs.io/en/latest/api.html#downloading

## Archive.org URL structure

### An item’s “details” page will always be available at
http://archive.org/details/[identifier]

### An item’s “metadata” will always be available at
http://archive.org/metadata/[identifier]

### The item directory is always available at
http://archive.org/download/[identifier]

### A particular file can always be downloaded from
http://archive.org/download/[identifier]/[filename]