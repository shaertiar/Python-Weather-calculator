import tkinter as tk
from tkinter import ttk
import time
import random

# Создание функции, которая будет "искать" погоду
def search_weather():
    global progress_bar, text

    # Функции обновления линии прогресса и текста
    def update():
        global progress_bar, text

        # Увеличение полоски загрузки
        if progress_bar['value'] < 100:
            progress_bar['value'] += random.randint(3, 9)

            if progress_bar['value'] > 100:
                progress_bar['value'] = 100

        # Изменение текста
        if progress_bar['value'] < 10:
            text['text'] = 'Отправка...'
        elif 10 <= progress_bar['value'] < 27:
            text['text'] = 'Получение...'
        elif 27 <= progress_bar['value'] < 81:
            text['text'] = 'Обработка...'
        elif 81 <= progress_bar['value'] < 99:
            text['text'] = 'Загрузка...'
        elif progress_bar['value'] == 100:
            text['text'] = 'Хз... Выгляни в окно.'

        # Обновление данных
        top.after(750, update)

    # Проверка на наличие написанного региона
    if entry.get() == '':
        text2.config(text='Не указан регион!')
    else:
        text2.config(text='')

        # Создание второго окна
        top = tk.Toplevel()
        top.geometry('320x240')
        top.resizable(False, False)
        top.title(f'Погода ({entry.get()})')

        # Создание линии прогресса
        progress_bar = ttk.Progressbar(top, orient='horizontal', length=300)

        # Создание текста
        text = tk.Label(top, text='')

        # Обновление данных
        top.after(100, update)

        # Размещение элементов
        progress_bar.pack()
        text.pack()

# Создание окна
root = tk.Tk()
root.geometry('320x240')
root.resizable(False, False)
root.title('Прогноз погоды')

# Создание бортика
frame = tk.LabelFrame(root, padx=20, pady=20)

# Создание текста
text1 = tk.Label(root, text='Прогноз погоды')
text2 = tk.Label(frame, text='')

# Создание поля для ввода
entry = tk.Entry(frame, width=35, borderwidth=5)
entry.insert(0, 'Щелково')

# Создание кнопки
button = tk.Button(frame, text='Узнать погоду в регионе', command=lambda: search_weather())

# Размещение элементов
text1.pack()
frame.pack(padx=10, pady=10)
entry.pack()
button.pack(pady=10)
text2.pack()

# Запуск приложения
root.mainloop()