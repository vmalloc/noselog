# Noselog

Noselog is a small [nose](http://nose.readthedocs.org/en/latest/) plugin that turns on logging for running tests. By default `nose` captures logs of running tests, but does not show them on the screen unless a failure occurrs. For debugging purposes, a user may want to see the logs as they run in certain situations

## Usage

Simply install noselog via `pip`:

    $ pip install noselog
    
And then, when running `nosetests`, append the `--with-noselog` flag:

    $ nosetests <nose options here> --with-noselog
    
## Additional options

* You can specify the file to log to with the `--noselog-file` option (by default, this is `-`, which means log to **stderr**). This option can be specified multiple times to log to multiple locations (e.g. both stderr and a file)
* You can specify the logging level with the `--noselog-level` option (by default, this is `DEBUG`)
* Console logging level is controlled separately (`DEBUG` by default) via the `--noselog-console-level` flag.
* Noselog can log test errors and failures (using `--noselog-log-errors` and `--noselog-log-failures`)
* You can specify a custom log format with the `--noselog-format`
  option. The default is "%(asctime)s %(name)s %(levelname)s -- %(message)s"
