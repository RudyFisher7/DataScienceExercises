

# (?:MSAMIATI|Msamiati|[1-9]\.\s*Maneno|Maneno|(?:[1-9]|1[0-9]|2[0-9])\s*|NB|Somo la)

with open('data/vocab_tables_raw.txt', 'r', encoding='utf-8') as file:
    raw = [next(file) for _ in range(96)]
    for line in raw:
        print(repr(line))