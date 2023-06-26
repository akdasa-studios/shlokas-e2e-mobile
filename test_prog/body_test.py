from test_prog.lib_classes.cls_new_driver import BaseDriver
from unittest import main as start_test


from test_prog import lib_tests as lt
from test_prog import lib_configs as lc

# -- start texts
BaseDriver.set_config(lc.config_sergei)
test_00 = lt.Test_01
# -- finish tests

if __name__ == '__main__':
    start_test()
