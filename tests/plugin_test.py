import unittest
from noseparallel import ParallelPlugin


class PluginTest(unittest.TestCase):
    def test_want_class_should_accept_on_either_nodes_but_not_both(self):
        class TestClass(unittest.TestCase):
            def test_method(self):
                pass

        plugin = ParallelPlugin()
        plugin.strategy = "CLASS"
        plugin.salt = "test"
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantClass(TestClass.__class__)

        plugin.node_index = 1
        rv1 = plugin.wantClass(TestClass.__class__)

        self.assertEqual({None, False}, {rv0, rv1})

    def test_want_directory_should_accept_on_either_nodes_but_not_both(self):
        directory = "dir"

        plugin = ParallelPlugin()
        plugin.strategy = "DIRECTORY"
        plugin.salt = "test"
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantDirectory(directory)

        plugin.node_index = 1
        rv1 = plugin.wantDirectory(directory)

        self.assertEqual({None, False}, {rv0, rv1})

    def test_want_file_should_accept_on_either_nodes_but_not_both(self):
        file = "file"

        plugin = ParallelPlugin()
        plugin.strategy = "FILE"
        plugin.salt = "test"
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantFile(file)

        plugin.node_index = 1
        rv1 = plugin.wantFile(file)

        self.assertEqual({None, False}, {rv0, rv1})

    def f(self):
        pass

    def test_want_method_should_accept_on_either_nodes_but_not_both(self):
        plugin = ParallelPlugin()
        plugin.strategy = "METHOD"
        plugin.salt = "test"
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
        plugin.strategy = "FUNCTION"
        plugin.salt = "test"
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantFunction(f)

        plugin.node_index = 1
        rv1 = plugin.wantFunction(f)

        self.assertEqual({None, False}, {rv0, rv1})

    def test_want_module_should_accept_on_either_nodes_but_not_both(self):
        def f():
            pass

        plugin = ParallelPlugin()
        plugin.strategy = "MODULE"
        plugin.salt = "test"
        plugin.total_nodes = 2

        plugin.node_index = 0
        rv0 = plugin.wantModule(f)

        plugin.node_index = 1
        rv1 = plugin.wantModule(f)

        self.assertEqual({None, False}, {rv0, rv1})
