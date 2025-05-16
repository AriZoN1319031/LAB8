# 8.3 — Работа с множествами: языки студентов

students = {
    "Алексей": {"английский", "русский"},
    "Мария": {"китайский", "английский"},
    "Иван": {"французский", "немецкий"},
    "Анна": {"русский", "китайский"},
    "Олег": {"испанский", "английский"},
}


all_languages = set()

for langs in students.values():
    all_languages.update(langs)

print("Различные языки, которые знают студенты:")
for lang in sorted(all_languages):
    print("-", lang)


print("\nСтуденты, знающие китайский язык:")
for name, langs in students.items():
    if "китайский" in langs:
        print("-", name)
