import tkinter as tk
import playaudio as pl
import asyncio

i = 0
clicks = 0
btn_press_delay = 500
win = 1
plus = 1


def coro_sound():
    pl.playaudio('hamburger-sound-effect.mp3')


def button_did():
    btn.configure(image=ham_bit_pic)
    global clicks
    clicks += win
    burger_count["text"] = f"Humgurgers {clicks}"
    btn.after(btn_press_delay, lambda: btn.configure(image=ham_pic))


def button2_did():
    global i
    if i > 0:
        pass
    else:
        shop_window = tk.Tk()
        shop_window.protocol("WM_DELETE_WINDOW", lambda: None)
        shop_window.title('Hamburger Shop')
        shop_window.resizable(False, False)
        shop_widow_x = shop_window.winfo_screenwidth() // 4
        shop_window_y = shop_window.winfo_screenheight() // 4
        shop_window.configure(background='black')
        shop_window.geometry(f'310x410+{shop_widow_x - 200}+{shop_window_y - 200}')
        i += 1

        btn_shop1 = tk.Button(shop_window, text='Close', bg='white', activebackground='black', borderwidth=0, command=lambda: button1_shop_did(
            shop_window))
        btn_shop1.config(height=5, width=10)
        btn_shop1.pack(side='bottom')

        btn_shop2 = tk.Button(shop_window, text='Buy', bg='white', activebackground='black', borderwidth=0, command=lambda: button2_shop_did(btn_shop2))
        btn_shop2.config(height=5, width=10)
        btn_shop2.pack(side='top')


def button3_did():
    window.quit()


def button1_shop_did(shop_window):
    shop_window.destroy()
    global i
    i -= 1


def button2_shop_did(btn_shop2):
    global plus
    global win
    global clicks
    if clicks < 10 * plus:
        pass
    else:
        clicks -= 10 * plus
        plus *= 2
        win += 1
        btn_shop2["text"] = f"Buying cost {10 * plus}"


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", lambda: None)
window.title('Hamburger')
window.resizable(False, False)
window_x = window.winfo_screenwidth()//2
window_y = window.winfo_screenheight()//2
window.configure(background='black')
window.geometry(f'510x410+{window_x - 200}+{window_y - 200}')

########################################################################################################################

ham_bit_pic = tk.PhotoImage(file='Bit_Hamburger.png')
ham_pic = tk.PhotoImage(file='pngwing2.png')
shop_pic = tk.PhotoImage(file='Good_Shop.png')
quit_pic = tk.PhotoImage(file='Без названия3_20231226010202.png')

########################################################################################################################

burger_count = tk.Label(window, text=f'Humgurgers {0}', bg='black', fg='white')
burger_count.pack(side='bottom')

########################################################################################################################

textus = tk.Label(window, text='Click on Hamburger', bg='black', fg='white')
textus.pack(side='top')

########################################################################################################################

btn = tk.Button(window, image=ham_pic, bg='black', activebackground='black', borderwidth=0, command=button_did)
btn.config(height=230, width=260)
btn.pack(anchor='center')

########################################################################################################################

btn2 = tk.Button(window, image=shop_pic, bg='black', activebackground='black', borderwidth=0, command=button2_did)
btn2.config(height=60, width=60)
btn2.pack(side='left')

########################################################################################################################

btn3 = tk.Button(window, image=quit_pic, bg='black', activebackground='black', borderwidth=0, command=button3_did)
btn3.config(height=60, width=60)
btn3.pack(side='right')

########################################################################################################################


window.mainloop()
