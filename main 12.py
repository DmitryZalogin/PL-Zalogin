import tkinter as tk
from tkinter import Entry, Button, scrolledtext, messagebox
import requests



def start():
    e = entry.get()
    if e == '2':
        # Имя пользователя github
        username = "spark"
        # url для запроса
        url = f"https://api.github.com/users/{username}"
        # делаем запрос и возвращаем json
        user_data = requests.get(url).json()
        # довольно распечатать данные JSON
        a = user_data
        a = {'company': f'{a['company']}', 'created_at': f'{a['created_at']}', 'email': f'{a['email']}', 'id': f'{a['id']}', 'name': f'{a['name']}', 'url': f'{a['url']}'}
        text_window.delete(1.0, tk.END)
        text_window.insert(1.0, f'{a}')
    else:
        text_window.delete(1.0, tk.END)
        text_window.insert(1.0, 'ошибка ввода')


#окно
window = tk.Tk()
window.title('ZaloginPl')
window.geometry('500x300')
window.resizable(height=False, width=False)


entry = Entry(window, width=30)
entry.grid(row=1, column=1)


button = Button(window, text='start', command=start)
button.grid(row=1, column=2)


text_window = scrolledtext.ScrolledText(window, width=45, height=16, fg='blue')
text_window.grid(row=2, column=1)


window.mainloop()