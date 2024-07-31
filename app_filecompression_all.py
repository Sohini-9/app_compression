import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog   #helps to open up any file which is presnt in the computer

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to compress")   #allows to select any file from the dialogue box that opens
    return filename

def compression(i,o):
    compress(i,o)

#create button for decompress and write the functions for them respectively

# input_entry = tk.Entry(window) :) write this after the window is created not here



window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")



compress_button = tk.Button(window,text="Compress",command=lambda: compression(open_file(),"output_context1.txt"))   #we are not simply using the function and using the lanbda function because it is more dynamic and as here the user will enter the file name to be compressed



compress_button.grid(row=2,column=2)

window.mainloop()