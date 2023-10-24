def read_md_file(file_name):
    """
    Эта функция читает содержимое файла с расширением .md и возвращает его текст.
    :param file_name:
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def split_md_file(file_content):
    """
    Эта функция разделяет содержимое файла на разделы на основе заголовков.
    :param file_content:
    :return:
    """
    headings = file_content.split('# ')
    headings.pop(0)
    result = []
    for heading in headings:
        lines = heading.split('\n')
        title = lines.pop(0)
        content = '\n'.join(lines)
        result.append(f"# {title}\n\n{content}")
    return result


def write_md_file(content, file_name):
    """
    Эта функция записывает указанное содержимое в файл с расширением .md.
    :param content:
    :param file_name:
    :return:
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)


file_name = 'example.md'

# Чтение файла
file_content = read_md_file(file_name)

# Разбивка по заголовкам
splitted_content = split_md_file(file_content)

# Запись файла
new_file_name = "new_example.md"
new_content = '\n'.join(splitted_content)
write_md_file(new_content, new_file_name)


input('\n\nНажмите "ENTER" для завершения.')
