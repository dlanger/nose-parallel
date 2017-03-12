import unittest
from noseparallel import ParallelPlugin


class PluginTest(unittest.TestCase):

    def f(self):
        pass

    def test_want_method_should_accept_on_either_nodes_but_not_both(self):
        plugin = ParallelPlugin()
        plugin.salt = 'test'
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantMethod(self.f)

        plugin.node_index = 1
        rv1 = plugin.wantMethod(self.f)

        self.assertEqual({None, False}, {rv0, rv1})

    def test_want_function_should_accept_on_either_nodes_but_not_both(self):

        def f():
            pass

        plugin = ParallelPlugin()
        plugin.salt = 'test'
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantFunction(f)

        plugin.node_index = 1
        rv1 = plugin.wantFunction(f)

        self.assertEqual({None, False}, {rv0, rv1})
