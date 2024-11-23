# Задаем имена файлов
input_filename = '3.txt'
output_filename = 'var3.txt'

# Открываем входной файл для чтения и выходной файл для записи
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        # Заменяем точки на запятые и убираем лишние пробелы
        modified_line = ' '.join(line.replace('.', ',').split())
        # Записываем изменённую строку в выходной файл
        outfile.write(modified_line + '\n')