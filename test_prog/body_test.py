from test_prog.lib_classes.cls_environment import Environment
from test_prog.lib_classes.cls_driver import BaseDriver
from unittest import main as start_test


from test_prog import lib_tests as lt
from test_prog import lib_configs as lc

Environment.enable_environment()

# -- start texts
BaseDriver.set_config(lc.config_00)
test_00 = lt.Test_00
# -- finish tests

if __name__ == '__main__':
    start_test()
