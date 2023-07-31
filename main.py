import tkinter as tk
from tkinter import Button
import keyboard

r = r'/Users/wallissonmartins/Desktop/Linguagens/Python/projetos/configurar_atalho_teclado/shortcuts.txt'
with open(r, mode='r', encoding='utf-8') as f:
    data = f.read()
print(data)
codeops = [x.split(',', maxsplit=1) for x in data.strip().splitlines()]
pr = '@'
for code in codeops:
    keyboard.add_abbreviation(f'{pr}{code[0]}',
                              code[1].replace(r'\\', '\\').replace('\\n', '\n'))


def stop_app():
    window.quit()

# while (g := input()) != 'exit':
    # sleep(1)


if __name__ == '__main__':
    window = tk.Tk()

    window.title('Atalhos personalizados')
    window.geometry('400x200')
    window.config(pady=80)

    button_exit = Button(window, text="Parar", width=30, command=stop_app, bg='#FF0000',
                         fg='white', activebackground='#990000', activeforeground='white', cursor='hand2')
    button_exit.pack()

    window.mainloop()
