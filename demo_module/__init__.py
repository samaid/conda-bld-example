#  __init__.py allows to see demo_module on import


def hello_init():
    print("Hello from __init__.py. It allows to import demo_module in demo.py and run: python demo.py")


def hello_main():
    print("Hello from __main__.py. It allows to execute: python -m demo_module")


def int_tuple(tuple_str):
    return tuple(map(int, tuple_str.split(",")))
