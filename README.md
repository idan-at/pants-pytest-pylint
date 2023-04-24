# pants pylint import error of pytest bug

Running `pants lint ::` will show pylint failure with this error:
```
in-here/a_test.py:2:0: E0401: Unable to import 'pytest' (import-error)
```
