import pytest

import parsl
from parsl import *

parsl.set_stream_logger()

from parsl.executors.swift_t import *


def foo(x, y):
    return x * y


def slow_foo(x, y):
    import time
    time.sleep(x)
    return x * y


def bad_foo(x, y):
    time.sleep(x)
    return x * y


@pytest.mark.local
def test_simple():
    print("Start")
    tex = TurbineExecutor()
    x = tex.submit(foo, 5, 10)
    print("Got: ", x)
    print("X result: ", x.result())
    assert x.result() == 50, "X != 50"
    print("done")


@pytest.mark.local
def test_slow():
    futs = {}
    tex = TurbineExecutor()
    for i in range(0, 3):
        futs[i] = tex.submit(slow_foo, 1, 2)

    total = sum([futs[i].result(timeout=10) for i in futs])
    assert total == 6, "expected 6, got {}".format(total)


@pytest.mark.local
def test_except():
    with pytest.raises(NameError):
        tex = TurbineExecutor()
        x = tex.submit(bad_foo, 5, 10)
        x.result()


if __name__ == "__main__":

    # test_simple()
    # test_slow()
    test_except()

    print("Done")
