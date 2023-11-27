# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart1
import chart2

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("500x500")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 16, 'bold'), fg = '#000066')
lblTitle.place(x=75, y=30)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=50, y=120, width=90, height=30)

lblChart1 = tk.Label(text = "График синуса matplotlib")
lblChart1.place(x=180, y=125)

# Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text="График 2", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=50, y=180, width=90, height=30)

lblChart2 = tk.Label(text = "ГНормальное распределение")
lblChart2.place(x=180, y=190)

#Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)


# Запуск цикла mainloop
window.mainloop()
