import json
import time

start_time = time.time()
# Функция для чтения данных из JSON файла
def read_json_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

# Функция для преобразования JSON в XML
def json_to_xml(data, indent_level=0):
    # Начальный отступ (для корня)
    indent = "  " * indent_level
    xml_string = ""

    # Преобразование словаря в XML
    if isinstance(data, dict):
        for key, value in data.items():
            # Создание элемента с тегом <key>
            xml_string += f"{indent}<{key}>\n"
            # Рекурсивное добавление содержимого
            xml_string += json_to_xml(value, indent_level + 1)
            # Закрытие тега </key>
            xml_string += f"{indent}</{key}>\n"

    # Преобразование списка в XML
    elif isinstance(data, list):
        for item in data:
            # Если это список, то добавляем <Lesson> для каждого элемента
            xml_string += f"{indent}<Lesson>\n"
            for subject, details in item.items():
                if subject != "Teacher":
                    xml_string += f"{indent}  <Subject>{subject}</Subject>\n"
                    xml_string += f"{indent}  <Details>{details}</Details>\n"
                else:
                    # Если это Teacher, добавляем его отдельно
                    xml_string += f"{indent}  <Subject>Teacher</Subject>\n"
                    xml_string += f"{indent}  <Details>{details}</Details>\n"
            xml_string += f"{indent}</Lesson>\n"

    # Преобразование строкового значения
    else:
        # Добавляем значение как текст в теги
        xml_string += f"{indent}{data}\n"

    return xml_string

# Функция для создания полного XML с заголовком
def create_xml(data):
    xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_string += "<Schedule>\n"  # Добавление тега <Schedule> после заголовка
    xml_string += json_to_xml(data, indent_level=1)
    xml_string += "</Schedule>\n"  # Закрытие тега <Schedule>
    return xml_string

# Чтение данных из файла
data = read_json_from_file('расписание.json')

# Преобразование данных в XML
xml_result = create_xml(data)

# Запись результата в файл
with open('task1.xml', 'w', encoding='utf-8') as file:
    file.write(xml_result)

print("XML файл успешно сохранен как 'task1.xml'.")
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")