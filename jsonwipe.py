import json


def wipe(filename: str):
    with open(f'{filename}.json', 'r', encoding='utf-8') as file:
        f = file.read()
        load = json.loads(f)
        for item in load.keys():
            load.update({item: ""})
        file.close()
    with open(f'{filename}.json', 'w', encoding='utf-8') as file:
        json.dump(load, file, ensure_ascii=False, indent=4)
        file.close()


if __name__ == '__main__':
    wipe('wiped')
