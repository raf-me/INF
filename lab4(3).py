import xml.etree.ElementTree as ET
import json
import time

def read_json_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Используем json.load, так как это безопаснее, чем eval
    return data

def json_to_xml(json_data, root_tag="person"):
    def dict_to_xml(data, parent):
        for key, value in data.items():
            if isinstance(value, dict):
                # Создаём новый элемент для вложенного словаря
                subelement = ET.SubElement(parent, key)
                dict_to_xml(value, subelement)
            elif isinstance(value, list):
                # Если это список, создаём отдельный элемент для каждого элемента в списке
                for item in value:
                    subelement = ET.SubElement(parent, key)
                    dict_to_xml({"hobby": item}, subelement)
            else:
                # Для базовых типов данных, просто добавляем текст
                ET.SubElement(parent, key).text = str(value)

    root = ET.Element(root_tag)
    dict_to_xml(json_data, root)
    return ET.tostring(root, encoding="unicode", method="xml")

data = read_json_from_file('расписание.json')
xml_result = json_to_xml(data)

with open('task3(1).xml', 'w', encoding='utf-8') as file:
    file.write(xml_result)

print("XML файл успешно сохранен как 'task3(1).xml'.")

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")
