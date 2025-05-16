# 8.2 — Подсчет очков в игре "Эрудит"

# словарь с баллами
points = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

# создаем обратный словарь: буква -> балл
letter_points = {}
for score, letters in points.items():
    for letter in letters:
        letter_points[letter] = score

word = input("Введите слово: ").upper()
total_score = 0

for letter in word:
    if letter in letter_points:
        total_score += letter_points[letter]

print("Стоимость слова:", total_score)
