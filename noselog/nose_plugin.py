import logging
from numbers import Number
import os
import sys
from nose.plugins import Plugin as NosePluginBase

class NosePlugin(NosePluginBase):
    name = 'noselog'
    def options(self, parser, env=os.environ):
        super(NosePlugin, self).options(parser, env)
        parser.add_option("--noselog-file", dest="outputfile", default="-")
        parser.add_option("--noselog-level", dest="level", default="DEBUG")

    def configure(self, options, conf):
        super(NosePlugin, self).configure(options, conf)
        if not self.enabled:
            return
        if options.outputfile == "-":
            handler = logging.StreamHandler(sys.stderr)
        else:
            handler = logging.FileHandler(options.outputfile)
        handler.setLevel(self._get_levelno(options.level))
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s -- %(msg)s"))
        logging.getLogger().addHandler(handler)
    def _get_levelno(self, level):
        if isinstance(level, Number):
            return level
        for level_name, levelno in logging._levelNames.items():
            if level_name == level:
                return levelno
        raise LookupError("Level name not found")

        


