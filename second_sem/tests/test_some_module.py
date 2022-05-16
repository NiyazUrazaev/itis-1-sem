from second_sem.lesson13.some_module.some_file import some_func
from second_sem.lesson13.some_module.some_file2 import some_func2
from .fixtures_ex import a_obj_fixture as some_fixture
from .fixtures_ex import yield_obj_fixture as yield_fixture
from ..lesson2.test import A


class TestSomeFile:
    def test_some_func_positive(self):
        assert some_func(3) == 9


    def test_some_func_negative(self):
        assert some_func(5) != 4


class TestSomeFile2:
    def test_some_func_positive(self):
        assert some_func2(3) == 27

    def test_some_func_negative(self):
        assert some_func2(5) != 4


class TestSomeFixture:
    def test_some_fixture(self, some_fixture):
        assert some_fixture.value == 1

    def test_some_fixture2(self, some_fixture):
        a_obj = A(2)
        assert a_obj < some_fixture

    def test_some_fixture3(self, yield_fixture):
        k = 1
        for i in yield_fixture:
            assert i == k
            k += 1