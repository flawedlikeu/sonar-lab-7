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
