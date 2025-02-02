import tkinter as tk
import tkinter.ttk as ttk
import create


def gen():
    if is_lang_fi.get() or is_lang_sv.get():
        frame.destroy()
        generating_text.place(x=100, y=80, anchor='s')
        #generating_bar.place(x=100, y=100, anchor='n')
        root.update()
        create.create(create.load_stops(['fi' * is_lang_fi.get(), 'sv' * is_lang_sv.get()]), 'en_us', done_text)
    else:
        errortext.place(x=100, y=160, anchor='s')

root = tk.Tk()
root.geometry('200x200')
root.resizable(False, False)
root.title('HSLcraft')
frame = ttk.Frame(root, width=200, height=200)

title = ttk.Label(root, text='HSLcraft\nresource pack generator v1.0\nby Dima\'s Notebook')
is_lang_fi = tk.BooleanVar(frame, value=True)
is_lang_sv = tk.BooleanVar(frame, value=False)
lang_fi = ttk.Checkbutton(frame, text='Use finnish names', variable=is_lang_fi, state=is_lang_sv)
lang_sv = ttk.Checkbutton(frame, text='Use swedish names', variable=is_lang_sv, state=is_lang_fi)
generate = ttk.Button(frame, text='Generate', command=gen)
errortext = ttk.Label(frame, text='At least one language\nmust be selected.', foreground='#FF0000')

generating_text = ttk.Label(root, text='Generating your resource pack')
gen_progress = tk.IntVar()
generating_bar = ttk.Progressbar(root, length=160, variable=gen_progress)
done_text = ttk.Label(root, text='Generation complete!\nCopy output.zip to your\nresource pack folder.')

title.place(x=10, y=10)
lang_fi.place(x=10, y=80)
lang_sv.place(x=10, y=100)
generate.place(x=100, y=190, anchor='s')
frame.pack()
root.mainloop()