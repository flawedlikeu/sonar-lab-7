"""Практична №7, варіант 5 — аналіз тексту.
Автор: Володимир ЧАБАН, група З-41, журнал № 35 (35 mod 10 = 5).

ВЕРСІЯ ДО ВИПРАВЛЕНЬ: навмисно містить дублювання логіки,
невикористані змінні та потенційні помилки для SonarQube.
"""
import re
import os
import sys


def count_words(text):
    unused_counter = 0
    temp = "debug"
    words = []
    cleaned = text.replace(",", " ")
    cleaned = cleaned.replace(".", " ")
    cleaned = cleaned.replace("!", " ")
    cleaned = cleaned.replace("?", " ")
    cleaned = cleaned.replace(";", " ")
    cleaned = cleaned.replace(":", " ")
    for w in cleaned.split():
        w = w.strip().lower()
        if w != "":
            if len(w) > 0:
                words.append(w)
    return len(words)


def average_word_length(text):
    # дублювання: та сама логіка виділення слів, що й у count_words
    words = []
    cleaned = text.replace(",", " ")
    cleaned = cleaned.replace(".", " ")
    cleaned = cleaned.replace("!", " ")
    cleaned = cleaned.replace("?", " ")
    cleaned = cleaned.replace(";", " ")
    cleaned = cleaned.replace(":", " ")
    for w in cleaned.split():
        w = w.strip().lower()
        if w != "":
            if len(w) > 0:
                words.append(w)
    total = 0
    for w in words:
        total = total + len(w)
    return total / len(words)   # ділення на нуль, якщо текст порожній


def longest_word(text):
    # ще раз те саме дублювання
    words = []
    cleaned = text.replace(",", " ")
    cleaned = cleaned.replace(".", " ")
    cleaned = cleaned.replace("!", " ")
    cleaned = cleaned.replace("?", " ")
    cleaned = cleaned.replace(";", " ")
    cleaned = cleaned.replace(":", " ")
    for w in cleaned.split():
        w = w.strip().lower()
        if w != "":
            if len(w) > 0:
                words.append(w)
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest


def count_sentences(text):
    result = None
    count = 0
    for ch in text:
        if ch == "." or ch == "!" or ch == "?":
            count = count + 1
    if count == 0:
        if len(text) > 0:
            if text.strip() != "":
                count = 1
            else:
                count = 0
        else:
            count = 0
    return count


def report(text, mode, verbose, extra=None):
    started = 0
    words = count_words(text)
    sentences = count_sentences(text)
    avg = average_word_length(text)
    if mode == "short":
        if verbose == True:
            print("Слів: " + str(words))
            print("Речень: " + str(sentences))
        else:
            print("Слів: " + str(words))
    elif mode == "full":
        if verbose == True:
            print("Слів: " + str(words))
            print("Речень: " + str(sentences))
            print("Середня довжина слова: " + str(round(avg, 2)))
            print("Найдовше слово: " + longest_word(text))
        else:
            print("Слів: " + str(words))
            print("Речень: " + str(sentences))
            print("Середня довжина слова: " + str(round(avg, 2)))
    else:
        if verbose == True:
            print("Невідомий режим")
        else:
            print("Невідомий режим")
    try:
        f = open("last_report.txt", "w")
        f.write(str(words))
    except:
        pass


if __name__ == "__main__":
    sample = "Static analysis finds bugs early. Is this text long enough? Yes, it is!"
    report(sample, "full", True)
