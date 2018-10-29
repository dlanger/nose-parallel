import os
import hashlib
import logging

from nose.plugins.base import Plugin

log = logging.getLogger('nose.plugin.parallel')


class ParallelPlugin(Plugin):
    name = 'parallel'

    TOTAL_NODES_POSSIBLE_VARIABLES = [
        'CIRCLE_NODE_TOTAL',
        'BUILDKITE_PARALLEL_JOB_COUNT',
        'NODE_TOTAL'
    ]

    INDEX_NODE_POSSIBLE_VARIABLES = [
        'CIRCLE_NODE_INDEX',
        'BUILDKITE_PARALLEL_JOB',
        'NODE_INDEX'
    ]

    def configure(self, options, config):
        super(ParallelPlugin, self).configure(options, config)
        self.salt = options.parallel_salt or os.environ.get(options.parallel_salt_env, '')
        self.total_nodes = self._parse_possible_variables(self.TOTAL_NODES_POSSIBLE_VARIABLES, default=1)
        self.node_index = self._parse_possible_variables(self.INDEX_NODE_POSSIBLE_VARIABLES, default=0)

    def _parse_possible_variables(self, possible_variables, default=None):
        for variable in possible_variables:
            value = os.environ.get(variable, None)
            if value is not None:
                return int(value)
        return default

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
