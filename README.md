# GitTheJob
In order to run jokeme.ksh, you will need to have Korn shell installed.  If /bin/ksh is NOT where Korn shell is located on your server, you will need to either:
 1. create a link /bin/ksh to it's actual location
 2. Update the header of the jokeme.ksh to reference python's actual location.

In order to run jokeme.py, you will need to have Python installed.  If /usr/bin/python is NOT where Python is located on your server, you will need to either:
 1. Create a link /usr/bin/python to it's actual location
 2. Update the header of the jokeme.py to reference python's actual location.

Both relative and full paths are acceptable when running either script as they determine where the input file is based on how you call the script.
