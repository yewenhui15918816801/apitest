import pytest


def funx(x):
    return x + 1


def test_answer():
    assert funx(6) == 5


# 创建一个test类的方法