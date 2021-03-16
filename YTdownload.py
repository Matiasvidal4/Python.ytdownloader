from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog
import os

folder_name = ""

gui = Tk()
gui.geometry("350x400")
gui.title("YTdownloader")
gui.columnconfigure(0, weight = 1)


def directory():
    global folder_name
    folder_name = filedialog.askdirectory()
    if len(folder_name) > 0:
        dir_error.config(text = folder_name, fg = "green")
    else:
        dir_error.config(text="DIR error", fg="red")


def url():    

    if len(entry_url.get()) > 1: 
        dlw_error.config(text = "", fg = "green")
        url_error.config(text = " ")
        yt = entry_url.get()
        titulo = YouTube(entry_url.get())
        if quality_option.get() == choices[0]:
            select = YouTube(yt).streams.filter(progressive = True, file_extension="mp4").order_by("resolution").desc().first()
        if quality_option.get() == choices[1]:
            select = YouTube(yt).streams.filter(only_audio = True).first()
            titulo2 = titulo.title


        select.download(output_path = folder_name, skip_existing = True)
        dlw_error.config(text = "Descarga completada", fg = "green")

        if quality_option.get() == choices[1]: 
            os.replace(folder_name+"/"+titulo2+".mp4" , folder_name+"/"+titulo2+".mp3" )
        





url_label = Label(gui, text="INGRESA LA URL DEL VIDEO", bg="red", fg="white", font=("helvetica", 12, "bold"))
url_label.grid()


entry_url = Entry(gui, width = 40, font = ("helvetica", 10))
entry_url.grid(pady = 20)

url_error = Label(gui, text=" ", fg="red", font=("helvetica", 8, "bold"))
url_error.place(y = 75, x = 145)

dir_label = Label(gui, text="SELECCIONA EL DIRECTORIO", fg="black", font=("jost", 11, "bold"))
dir_label.grid(pady = 10)

dir_button = Button(gui, width = 20, bg = "red",fg = "white", text = "directorio", command = lambda: directory())
dir_button.grid()

dir_error = Label(gui, text=" ", fg="red", font=("helvetica", 8, "bold"))
dir_error.grid()

quality_label = Label(gui, text="SELECCIONA LA CALIDAD", fg="black", font=("jost", 11, "bold"))
quality_label.grid(pady = 10)

choices = ["Video y audio", "Solo audio"]
quality_option = ttk.Combobox(gui, values = choices)
quality_option.grid()
quality_error = Label(gui, text=" ", fg="red", font=("jost", 8, "bold"))
quality_error.grid()

download_button = Button(gui, width = 20, bg = "red",fg = "white", text = "DESCARGAR", command = lambda: url())
download_button.grid(pady = 30)

dlw_error = Label(gui, text=" ", fg="red", font=("jost", 8, "bold"))
dlw_error.grid()




gui.mainloop()


