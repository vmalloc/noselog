import logging
from numbers import Number
import os
import sys
from nose.plugins import Plugin as NosePluginBase

class NosePlugin(NosePluginBase):
    name = 'noselog'
    def options(self, parser, env=os.environ):
        super(NosePlugin, self).options(parser, env)
        parser.add_option("--noselog-file", dest="outputfiles", default=[], action="append",
                          help="Output files to log to. '-' means stderr. Can be specified multiple times.")
        parser.add_option("--noselog-console-level", dest="console_level", default="DEBUG")
        parser.add_option("--noselog-level", dest="level", default="DEBUG")

    def configure(self, options, conf):
        super(NosePlugin, self).configure(options, conf)
        if not self.enabled:
            return
        outputfiles = options.outputfiles
        if not outputfiles:
            outputfiles = ["-"]

        for output_file_name in set(outputfiles):
            if output_file_name == "-":
                handler = logging.StreamHandler(sys.stderr)
                handler.setLevel(self._get_levelno(options.console_level))
            else:
                handler = logging.FileHandler(output_file_name)
                handler.setLevel(self._get_levelno(options.level))
            handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s -- %(message)s"))
            logging.getLogger().addHandler(handler)
    def _get_levelno(self, level):
        if isinstance(level, Number):
            return level
        for level_name, levelno in logging._levelNames.items():
            if level_name == level:
                return levelno
        raise LookupError("Level name not found")
