import tkinter as tk
from compressmodule import compress,decompress


def compression(i,o):
    compress(i,o)

#create button for decompress and write the functions for them respectively

# input_entry = tk.Entry(window) :) write this after the window is created not here

window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")

input_entry = tk.Entry(window)
output_entry =tk.Entry(window)

input_entry.grid(row=0,column=1)
output_entry.grid(row=1,column=1)

compress_button = tk.Button(window,text="Compress",command=lambda: compression(input_entry.get(),output_entry.get()))   #we are not simply using the function and using the lanbda function because it is more dynamic and as here the user will enter the file name to be compressed

input_label = tk.Label(window,text="File to be compressed")
output_label = tk.Label(window,text="Name of the compressed file")
input_label.grid(row=0,column=0) 
output_label.grid(row=1,column=0)

compress_button.grid(row=2,column=2)

window.mainloop()