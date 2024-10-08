import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize("str, result",
[("tes1", "Test1"),
    ("t","T"),
    ("capitilize test", "Capitilize test"),
    ("Test", "Test"),
    ("TEST", "Test"),
    ("123test", "123test"),
    (" test", " test"),
    ("", "")])

def test_capitilize(str, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(str)
    assert res == result

@pytest.mark.parametrize("str, result",
[(" test trim", "test trim"),
("  test trim", "test trim"),
("test trim", "test trim"),
(" ", ""),
("", "")])

def test_trim(str, result):
    string_utils = StringUtils()
    res = string_utils.trim(str)
    assert res == result


@pytest.mark.parametrize("str, delimeter, result",
[("a,b,c,d", ",", ["a", "b", "c", "d"]),
("1:2:3", ":", ["1", "2", "3"]),
("a-1", "-", ["a", "1"]),
("a.a, a.b, a.c", ", ", ["a.a", "a.b", "a.c"]),
("", "", [])])

def test_to_list(str, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(str, delimeter)
    assert res == result

@pytest.mark.parametrize("str, symbol, result",
[("test contains", "t", True),
("test contains", "test", True),
("test contains", "", True),
("test contains", "b", False),
("test contains", "T", False),
("test2", "2", True)])

def test_contains(str, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result",
[("delete symbol", "d", "elete symbol"),
("delete", "e", "dlt"),
("delete symbol", " ", "deletesymbol"),
("delete symbol", "D", "delete symbol"),
("delete symbol", "w", "delete symbol")])

def test_delete_symbol(str, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result",
[("starts with", "s", True),
("starts with", "w", False),
("starts_with", "S", False),
(" ", " ", True),
(" starts_with", "", True)])

def test_starts_with(str, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result",
[("end with", "h", True),
("end with", "d", False),
("ens_with", "H", False),
(" ", " ", True),
("end with ", "", True)])

def test_end_with(str, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, result",
[("", True),
("d", False),
("   ", True)])

def test_is_empty(str, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(str)
    assert res == result


@pytest.mark.parametrize("lst, joiner, result",
[([1,2,3,4], ", ", "1, 2, 3, 4"),
(["list", "string"], "_", "list_string"),
([], "", "")])

def test_list_to_string(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result