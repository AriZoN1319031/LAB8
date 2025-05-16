# 8.1 — Словарь стран и столиц

countries = {
    "Россия": "Москва",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Италия": "Рим",
    "Япония": "Токио"
}

print("Список стран и столиц:")
for country, capital in countries.items():
    print(f"{country} — {capital}")
country_input = input("Введите название страны: ")
if country_input in countries:
    print("Столица:", countries[country_input])
else:
    print("Такой страны нет в списке.")
print("\nСтраны по алфавиту:")
for country in sorted(countries):
    print(f"{country} — {countries[country]}")
