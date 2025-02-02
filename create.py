import json
import random
import shutil
import os
import tkinter.ttk as tk


def set_var(var, val):
    if var is not None:
        var.step(val)
        #win.update()


def create(stops: list, file: str, done=None, var: tk.Progressbar | None=None, window=None, **kwargs):
    f = load(file)
    global win
    win = window
    set_var(var, 20)
    keys = f.keys()
    stop_num = 0
    for stop in keys:
        stop_num += 1
        random_stop = random.choice(stops)
        f.update({stop: random_stop})
        set_var(var, 20 + int(stop_num / len(keys)) * 60)
        # stops.remove(random_stop)
    create_pack(f, kwargs)
    set_var(var, 100)
    if done is not None:
        done.place(x=100, y=130, anchor='n')


def create_pack(data: dict, args):
    if not os.path.exists('output'):
        os.makedirs('output')
    shutil.copy('hslcraft.png', 'output/pack.png')
    with open('output/pack.mcmeta', 'w') as f:
        f.write('''{
  "pack": {
    "pack_format": 32,
    "description": "Generated with HSLcraft by Dima's Notebook."
  }
}''')
    if not os.path.exists('output/assets/minecraft/lang'):
        os.makedirs('output/assets/minecraft/lang')
    write('output/assets/minecraft/lang/en_us', data)
    if not os.path.exists('output/assets/minecraft/textures/gui/title'):
        os.makedirs('output/assets/minecraft/textures/gui/title')
    shutil.copy('hslcraft.png', 'output/assets/minecraft/textures/gui/title/minecraft.png')
    shutil.make_archive('output', 'zip', 'output')


def load(file: str):
    file = open(f'{file}.json', 'r', encoding='utf-8')
    file_read = file.read()
    return json.loads(file_read)


def write(file: str, data: dict):
    with open(f'{file}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_stops(langs, file: str = 'translations'):
    with open(f'{file}.txt', 'r', encoding='utf-8') as file:
        f = file.read()
        f = f.split('\n')[:-1]
        stops = list()
        for line in f:
            stop = line.split(',')
            if stop[1] == '"stop_name"':
                if 'fi' in langs:
                    stops.append(stop[6][1:-1])
                if 'sv' in langs:
                    stops.append(stop[3][1:-1])
    return stops


if __name__ == '__main__':
    args = {"langs": ["fi", "sv"]}
    stop_list = load_stops(args["langs"])
    create(stop_list, 'en_us')
    print('Done! The output resource pack is "output.zip".')
