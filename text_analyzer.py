"""Практична №7, варіант 5 — аналіз тексту.
Автор: Володимир ЧАБАН, група З-41, журнал № 35 (35 mod 10 = 5).

Виправлена версія: спільна функція виділення слів замість дублювання,
без невикористаних змінних і параметрів, безпечне ділення,
конкретні винятки та константи для повторюваних рядків.
"""
import re

WORD_PATTERN = re.compile(r"[^\W\d_]+(?:['’-][^\W\d_]+)*")
SENTENCE_END = re.compile(r"[.!?]+")

LABEL_WORDS = "Слів: "
LABEL_SENTENCES = "Речень: "
LABEL_AVG = "Середня довжина слова: "
LABEL_LONGEST = "Найдовше слово: "


def extract_words(text):
    """Повертає список слів тексту (єдине місце з логікою розбиття)."""
    return [w.lower() for w in WORD_PATTERN.findall(text)]


def count_words(text):
    return len(extract_words(text))


def average_word_length(text):
    words = extract_words(text)
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def longest_word(text):
    return max(extract_words(text), key=len, default="")


def count_sentences(text):
    if not text.strip():
        return 0
    parts = [p for p in SENTENCE_END.split(text) if p.strip()]
    return max(len(parts), 1)


def build_report(text, mode="full"):
    """Формує рядки звіту; mode: 'short' або 'full'."""
    if mode not in ("short", "full"):
        raise ValueError(f"Невідомий режим: {mode}")
    lines = [LABEL_WORDS + str(count_words(text)), LABEL_SENTENCES + str(count_sentences(text))]
    if mode == "full":
        lines.append(LABEL_AVG + str(round(average_word_length(text), 2)))
        lines.append(LABEL_LONGEST + longest_word(text))
    return lines


def save_report(lines, path="last_report.txt"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    except OSError as err:
        print(f"Не вдалося зберегти звіт: {err}")


if __name__ == "__main__":
    sample = "Static analysis finds bugs early. Is this text long enough? Yes, it is!"
    report_lines = build_report(sample)
    print("\n".join(report_lines))
    save_report(report_lines)
