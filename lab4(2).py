import ast  #Безопасный парсинг, где используется анализируется структура данных без использования кода
import re
import time

start_time = time.time()

# Функция для чтения данных из файла и конвертации JSON в структуру Python
def read_json_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # Считываем содержимое файла
        json_str = file.read()
        # Преобразуем строку в Python-словарь с помощью ast.literal_eval
        data = ast.literal_eval(json_str)  # Безопасный способ преобразования
        return data


# Функция для преобразования Python-словаря в XML с использованием регулярных выражений
def json_to_xml(data):
    # Начало XML документа
    xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<Schedule>\n'

    # Проходим по дням
    for day, lessons in data.items():
        xml_output += f'  <{day}>\n'  # Добавляем день в XML
        # Проходим по каждому уроку в день
        for lesson in lessons:
            xml_output += f'    <Lesson>\n'
            for subject, details in lesson.items():
                # Применяем регулярные выражения для корректной обработки
                subject = re.sub(r'["\']', '', subject)  # Удаляем кавычки
                details = re.sub(r'["\']', '', details)  # Удаляем кавычки

                # Добавляем информацию по предмету и детали
                xml_output += f'      <Subject>{subject}</Subject>\n'
                xml_output += f'      <Details>{details}</Details>\n'
            xml_output += f'    </Lesson>\n'
        xml_output += f'  </{day}>\n'

    xml_output += '</Schedule>'  # Конец XML документа
    return xml_output


# Читаем данные из файла
data = read_json_from_file('расписание.json')

# Преобразуем данные в XML
xml_result = json_to_xml(data)

# Запись результата в файл
with open('task2.xml', 'w', encoding='utf-8') as file:
    file.write(xml_result)

print("XML файл успешно сохранен как 'outfile.xml'.")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")