# Noselog

Noselog is a small [nose](http://nose.readthedocs.org/en/latest/) plugin that turns on logging for running tests. By default `nose` captures logs of running tests, but does not show them on the screen unless a failure occurrs. For debugging purposes, a user may want to see the logs as they run in certain situations

## Usage

Simply install noselog via `pip`:

    $ pip install noselog
    
And then, when running `nosetests`, append the `--with-noselog` flag:

    $ nosetests <nose options here> --with-noselog
    
## Additional options

* You can specify the file to log to with the `--noselog-file` option (by default, this is `-`, which means log to **stderr**)
* You can specify the logging level with the `--noselog-level` option (by default, this is `DEBUG`)



