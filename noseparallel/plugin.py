import os
import hashlib
import logging

from nose.plugins.base import Plugin

log = logging.getLogger('nose.plugin.parallel')


class ParallelPlugin(Plugin):
    name = 'parallel'

    def configure(self, options, config):
        super(ParallelPlugin, self).configure(options, config)
        self.salt = options.parallel_salt or os.environ.get(options.parallel_salt_env, '')
        self.total_nodes = int(os.environ.get('CIRCLE_NODE_TOTAL') or os.environ.get('NODE_TOTAL', 1))
        self.node_index = int(os.environ.get('CIRCLE_NODE_INDEX') or os.environ.get('NODE_INDEX', 0))

    def wantMethod(self, method):
        try:
            return self._pick_by_name(method.__name__)
        except AttributeError:
            return None
        return None

    def wantFunction(self, function):
        try:
            return self._pick_by_name(function.__name__)
        except AttributeError:
            return None
        return None

    def _pick_by_name(self, name):
        m = hashlib.md5(self.salt.encode('utf-8'))
        m.update(name.encode('utf-8'))
        class_numeric_id = int(m.hexdigest(), 16)
        if class_numeric_id % self.total_nodes == self.node_index:
            return None
        return False

    def options(self, parser, env=os.environ):
        parser.add_option("--parallel-salt")
        parser.add_option("--parallel-salt-env", default="NOSE_PARALLEL_SALT")
        super(ParallelPlugin, self).options(parser, env=env)
