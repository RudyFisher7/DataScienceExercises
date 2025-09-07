import fitz
import re
import pypdf_table_extraction


swahili_pdf = fitz.open('data/Swahili - a foundation for speaking reading and writing (Hinnebusch _ Mirza).pdf')


# v1
def do_v1(pdf: fitz.Document) -> list[str]:
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

    return text_blocks


# v2
def do_v2(pdf: fitz.Document) -> list[str]:
    vocab_tables_lines_raw: list[str] = []

    chapter_regex1 = r'[1-9]|1[0-9]|2[0-9]+'
    chapter_regex2 = r'Somo la'
    vocab_start_regex = r'MSAMIATI'
    start_regex = r'(?:[1-9]|1[0-9]|2[0-9]).\s*Maneno|^Maneno'
    end_regex = r'NB: The vocab|The sentences|kumi na nane|ishirini na tatu|ishirini na tisa|Note that some|arobaini na nne|hamsini na mbili|hamsini na nane|sitini na tano|sabini na tatu|themanini|themanini na sita|tisini na saba|mia moja na nne|mia moja kumi na tatu|mia moja ishirini na moja|mia moja ishirini na nane|mia moja thelathini na tano|mia moja arobaini na nne|mia moja hamsini na moja|mia moja hamsini na nane|mia moja sitini na tano|mia moja sabini na tatu|mia moja themanini na moja|mia moja themanini na saba|mia moja tisini na nne|mia mbili'
    end_regs = end_regex.split('|')
    chapters = []

    i = 1
    j = 0
    cur_chapter = 0
    prev_chapter = 0
    started_chapter = False
    for page in pdf:
        if i >= 25 and i <= 224:
            page_text = page.get_textpage().extractText()
            lines = page_text.splitlines()

            for m in range(len(lines)):
                needle = re.match(chapter_regex1, lines[m])
                if bool(needle) and (m + 1) < len(lines):
                    m += 1
                    needle2 = re.match(chapter_regex2, lines[m])
                    if bool(needle2):
                        prev_chapter = cur_chapter
                        cur_chapter += 1
                        chapters.append(f'\s*{lines[m]}\s*')
                        # print(f'CHAPTER {cur_chapter}: {lines[m]}')
                        # print(re.match(chapters[len(chapters) - 1], lines[m]).string)
        i += 1

    matched_patterns = []
    i = 1
    for page in pdf:
        if i >= 25 and i <= 224:
            page_text = page.get_textpage().extractText()
            lines = page_text.splitlines()
            for m in range(len(lines)):
                n = re.match(end_regex, lines[m], re.IGNORECASE)
                if bool(n):
                    j += 1
                    j2 = j - 1
                    matched_patterns.append(n.string)
                    print(f'{j}: {lines[m]} => {n.string} -- {end_regs[j2] if j2 < len(end_regs) else 'out of range'}')
        i += 1

    for g in range(len(matched_patterns)):
        matched_patterns[g] = matched_patterns[g].strip()
    p = set(matched_patterns)
    e = set(end_regs)
    print(e.issubset(p))
    print(e.difference(p))

    exit()

    i = 1
    cur_chapter = 0
    for page in pdf:
        if i >= 25 and i <= 224:
            page_text = page.get_textpage().extractText()
            lines = page_text.splitlines()

            if not started_chapter:
                for m in range(len(lines)):
                    needle2 = re.match(chapters[cur_chapter], lines[m])
                    if bool(needle2):
                        started_chapter = True
                        print(f'CHAPTER {cur_chapter + 1}: {lines[m]}')
                        vocab_tables_lines_raw.append(f'CHAPTER {cur_chapter}: {lines[m]}\n')
                        cur_chapter += 1
            
            if started_chapter:
                vocab_started = False
                for m in range(len(lines)):
                    if not vocab_started:
                        needle = re.match(vocab_start_regex, lines[m], re.IGNORECASE)
                        if bool(needle):
                            vocab_tables_lines_raw.append('MSAMIATI\n')
                            vocab_started = True
                            # print(lines[m])
                    else:
                        end_needle = re.match(end_regex, lines[m], re.IGNORECASE)
                        needle = re.match(start_regex, lines[m], re.IGNORECASE)

                        if not bool(needle) and not bool(end_needle):
                            vocab_tables_lines_raw.append(f'{lines[m]}\n')
                        else:
                            if bool(end_needle):
                                started_chapter = False
                                vocab_tables_lines_raw.append('END MSAMIATI\n')
                                print(f'ended chapter: {cur_chapter}')

        i += 1
    print(i)
    return vocab_tables_lines_raw


text_blocks = do_v2(swahili_pdf)

swahili_pdf.close()

with open('data/vocab_tables_raw.txt', 'w') as file:
    for block in text_blocks:
        file.write(block)

# for block in text_blocks:
#     print(block)