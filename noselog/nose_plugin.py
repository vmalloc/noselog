import logging
from numbers import Number
import os
import sys
from nose.plugins import Plugin as NosePluginBase

_logger = logging.getLogger(__name__)

class NosePlugin(NosePluginBase):
    name = 'noselog'
    def options(self, parser, env=os.environ):
        super(NosePlugin, self).options(parser, env)
        parser.add_option("--noselog-file", dest="outputfiles", default=[], action="append",
                          help="Output files to log to. '-' means stderr. Can be specified multiple times.")
        parser.add_option("--noselog-console-level", dest="console_level", default="DEBUG")
        parser.add_option("--noselog-level", dest="level", default="DEBUG")
        parser.add_option("--noselog-logger", dest="additional_loggers", default=[], action="append", help="Specify additional logger names to include in captured logs")
        parser.add_option("--noselog-log-errors", dest="log_errors", default=False, action="store_true", help="Also log test errors")
        parser.add_option("--noselog-log-failures", dest="log_failures", default=False, action="store_true", help="Also log test failures (assertions etc.)")

    def configure(self, options, conf):
        super(NosePlugin, self).configure(options, conf)
        if not self.enabled:
            return
        self._options = options
        outputfiles = options.outputfiles
        if not outputfiles:
            outputfiles = ["-"]

        noselog_level = self._get_levelno(options.level)
        noselog_console_level = self._get_levelno(options.console_level)

        loggers_to_fix = [_logger, logging.getLogger()]
        loggers_to_fix.extend(map(logging.getLogger, options.additional_loggers))

        for logger in loggers_to_fix:
            logger.setLevel(noselog_level)

        for output_file_name in set(outputfiles):
            if output_file_name == "-":
                handler = logging.StreamHandler(sys.stderr)
                handler.setLevel(noselog_console_level)
            else:
                handler = logging.FileHandler(output_file_name)
                handler.setLevel(noselog_level)
            handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s -- %(message)s"))
            for logger in loggers_to_fix:
                logger.addHandler(handler)

    def addError(self, test, err):
        if self._options.log_errors:
            _logger.error("Error in test %s", test, exc_info=err)
    def addFailure(self, test, err):
        if self._options.log_failures:
            _logger.error("Failure in test %s", test, exc_info=err)

    def _get_levelno(self, level):
        if isinstance(level, Number):
            return level
        for level_name, levelno in logging._levelNames.items():
            if level_name == level:
                return levelno
        raise LookupError("Level name not found")
