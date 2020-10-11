import requests
from tkinter import *
from PIL import ImageTk, Image

bought_value = 249.47


def get_price():
    global bought_price
    try:
        bought_price = float(e.get())
    except ValueError:
        e.delete(0, END)
        e.insert(0, 'digite apenas números!')


def format_response(price):
    past_crypto_price = 0

    if ticker == 'BTC':
        past_crypto_price = 49657.10
    elif ticker == 'ETH':
        past_crypto_price = 1245.18
    elif ticker == 'XTZ':
        past_crypto_price = 16.07
    elif ticker == 'ADA':
        past_crypto_price = 0.660988
    elif ticker == 'TRX':
        past_crypto_price = 0.090766
    elif ticker == 'BNT':
        past_crypto_price = 7.73
    elif ticker == 'ATOM':
        past_crypto_price = 20.38
    elif ticker == 'BAND':
        past_crypto_price = 13.55
    current_price = (price * bought_price) / past_crypto_price

    return 'Preço atual: %s \npreço comprado: %s' % (current_price, bought_price)


def get_coin(symbol):
    global ticker
    ticker = symbol
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol,
        'convert': 'BRL'

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'c71ba770-c8f9-4726-8240-b48eaf31f3a8',
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    price = data['data'][symbol]['quote']['BRL']['price']

    label['text'] = format_response(price)


width = 800
height = 600

root = Tk()
root.title("check price")

background_image = ImageTk.PhotoImage(file='gadsden.jpg')
background_label = Label(root, image=background_image)
background_label.pack()

# for size
canvas = Canvas(root, height=height, width=width)
canvas.pack()

# frame
higher_frame = Frame(root, bg='#D6E820', bd=5)
higher_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.3, anchor='s')

label = Label(higher_frame)
label.place(relwidth=1, relheight=1)

lower_frame = Frame(root, bg='#D6E820', bd=5)
lower_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.35, anchor='n')
# button command
button_BTC = Button(lower_frame, text='BTC', command=lambda: get_coin('BTC'))
button_XTZ = Button(lower_frame, text='XTZ', command=lambda: get_coin('XTZ'))
button_ADA = Button(lower_frame, text='ADA', command=lambda: get_coin('ADA'))
button_ETH = Button(lower_frame, text='ETH', command=lambda: get_coin('ETH'))
button_TRX = Button(lower_frame, text='TRX', command=lambda: get_coin('TRX'))
button_BNT = Button(lower_frame, text='BNT', command=lambda: get_coin('BNT'))
button_ATOM = Button(lower_frame, text='ATOM', command=lambda: get_coin('ATOM'))
button_BAND = Button(lower_frame, text='BAND', command=lambda: get_coin('BAND'))
# get price frame
middle_frame = Frame(root, bg='#2D2F1A', bd=5)
middle_frame.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.05, anchor='n')
price_button = Button(middle_frame, text='preço de compra', command=get_price)
price_button.place(relx=0.7, relheight=0.9, relwidth=0.3)
e = Entry(middle_frame)
e.place(relwidth=0.69, relheight=0.9)

# button execution
button_BTC.place(relx=0, relheight=0.4, relwidth=0.5)
button_ETH.place(relx=0.5, relheight=0.4, relwidth=0.5)
button_ADA.place(relx=0, rely=0.4, relheight=0.2, relwidth=0.5)
button_XTZ.place(relx=0.5, rely=0.4, relheight=0.2, relwidth=0.5)
button_TRX.place(relx=0, rely=0.6, relheight=0.2, relwidth=0.5)
button_BNT.place(relx=0.5, rely=0.6, relheight=0.2, relwidth=0.5)
button_ATOM.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.5)
button_BAND.place(relx=0.5, rely=0.8, relheight=0.2, relwidth=0.5)


root.mainloop()
