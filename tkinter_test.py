import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text='このPCは重大なウィルスに感染しました', width=40)
button.pack(padx=10,pady=10)

clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text='保存されているパスワードを外部サーバーに送信します')
    elif clickCount == 2:
        button.configure(text='ブラウザ履歴を外部サーバーに送信します')
    else:
        button.pack_forget()

button.bind('<ButtonRelease-1>', onClick)
window.mainloop()
