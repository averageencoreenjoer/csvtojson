# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        data = []
        for row in csv_reader:
            entry = {}
            for i, value in enumerate(row):
                entry[headers[i]] = value

            data.append(entry)

    # TODO Сериализовать в файл с отступами равными 4
    json_data = json.dumps(data, indent=4)
    with open(OUTPUT_FILENAME, 'w') as output_file:
        output_file.write(json_data)  


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
