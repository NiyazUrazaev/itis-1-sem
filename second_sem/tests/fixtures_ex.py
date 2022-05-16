import pytest

from second_sem.lesson2.test import A


@pytest.fixture()
def a_obj_fixture():
    return A(1)


@pytest.fixture()
def yield_obj_fixture():
    yield [1, 2, 3]