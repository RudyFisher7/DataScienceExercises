import fitz
import re
import pypdf_table_extraction


pdf = fitz.open('data/Swahili - a foundation for speaking reading and writing (Hinnebusch _ Mirza).pdf')
text = ''
text_blocks = []

has_start = False
has_end = False
i = 1
next_chapter = 2
for page in pdf:
    if i >= 25 and i <= 224:
        page_text = page.get_textpage().extractText()
        if not has_start:
            if re.findall('MSAMIATI', page_text) or re.findall('Msamiati', page_text):
                has_start = True
        if not has_end:
            if re.findall(f"({next_chapter})\s*Somo la", page_text) or re.findall('Masomo Zaidi', page_text):
                has_end = True
                next_chapter += 1
        if re.findall('The following readings', page_text):
            print('found')
        if has_start:
            text += page_text

        if has_start and has_end:
            text_blocks.append(text)
            text = ''
            has_start = False
            has_end = False
    
    i += 1

pdf.close()

with open('data/vocab_tables_raw.txt', 'w') as file:
    for block in text_blocks:
        file.write(block)

for block in text_blocks:
    print(block)