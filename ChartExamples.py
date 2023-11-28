# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart1
import chart2
import chart3

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("550x500")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 16, 'bold'), fg = '#000066')
lblTitle.place(x=75, y=30)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=50, y=115, width=90, height=30)

lblChart1 = tk.Label(text = "График синуса matplotlib")
lblChart1.place(x=180, y=125)

# Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text="График 2", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=50, y=155, width=90, height=30)

lblChart2 = tk.Label(text = "Нормальное распределение")
lblChart2.place(x=180, y=165)

# Добавление кнопки и метки для графика 3
btnChart3 = tk.Button(window, text="График 3", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart3.place(x=50, y=195, width=90, height=30)

lblChart3 = tk.Label(text = "График matplotlib_legend")
lblChart3.place(x=180, y=205)

# Добавление кнопки и метки для графика 4
btnChart4 = tk.Button(window, text="График 4", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart4.place(x=50, y=235, width=90, height=30)

lblChart4 = tk.Label(text = "Нормальное распределение 3 графика")
lblChart4.place(x=180, y=245)

# Добавление кнопки и метки для графика 5
btnChart5 = tk.Button(window, text="График 5", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart5.place(x=50, y=275, width=90, height=30)

lblChart5 = tk.Label(text = "График matplotlib_legend")
lblChart5.place(x=180, y=285)

# Добавление кнопки и метки для графика 6
btnChart6 = tk.Button(window, text="График 6", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart6.place(x=50, y=315, width=90, height=30)

lblChart6 = tk.Label(text = "График matplotlib_legend")
lblChart6.place(x=180, y=325)

# Добавление кнопки и метки для графика 7
btnChart7 = tk.Button(window, text="График 7", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart7.place(x=50, y=355, width=90, height=30)

lblChart7 = tk.Label(text = "График matplotlib_legend")
lblChart7.place(x=180, y=365)

# Добавление кнопки и метки для графика 8
btnChart8 = tk.Button(window, text="График 8", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart8.place(x=50, y=395, width=90, height=30)

lblChart8 = tk.Label(text = "График matplotlib_legend")
lblChart8.place(x=180, y=405)

#Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=420, y=450, width=90, height=30)


# Запуск цикла mainloop
window.mainloop()
