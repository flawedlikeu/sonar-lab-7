from text_analyzer import average_word_length, build_report, count_sentences, count_words, longest_word

TEXT = "Static analysis finds bugs early. Is this text long enough? Yes, it is!"


def test_counts():
    assert count_words(TEXT) == 13
    assert count_sentences(TEXT) == 3


def test_empty_text_has_no_division_by_zero():
    assert average_word_length("") == 0.0
    assert count_sentences("   ") == 0
    assert longest_word("") == ""


def test_report_full():
    assert build_report(TEXT)[3] == "Найдовше слово: analysis"


def test_report_short_has_two_lines():
    assert build_report(TEXT, "short") == ["Слів: 13", "Речень: 3"]


def test_unknown_mode_is_rejected():
    import pytest
    with pytest.raises(ValueError):
        build_report(TEXT, "huge")


def test_save_report(tmp_path):
    from text_analyzer import save_report
    target = tmp_path / "r.txt"
    save_report(["a", "b"], str(target))
    assert target.read_text(encoding="utf-8") == "a\nb"


def test_save_report_bad_path_does_not_crash(capsys):
    from text_analyzer import save_report
    save_report(["a"], "/nonexistent-dir/r.txt")
    assert "Не вдалося зберегти звіт" in capsys.readouterr().out
