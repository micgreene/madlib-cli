import pytest
from madlib_cli.madlib import read_template, parse_template, merge, validate, wrapper


def test_read_template_returns_stripped_string():
    actual = read_template("../assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():
    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_validate_passes_correct_word():
    word = 'Adjective'
    user_input = 'yellow'
    actual = validate(word, user_input)
    expected = 'yellow'
    assert actual == expected

def test_validate_passes_correct_number():
    word = 'Number'
    user_input = '10'
    actual = validate(word, user_input)
    expected = '10'
    assert actual == expected

def test_wrapper():
    stringy = 'Test'
    actual = wrapper(stringy)
    expected = f'''\n\n<>============================================================<>\n{stringy}\n<>============================================================<>\n\n'''
    assert actual == expected