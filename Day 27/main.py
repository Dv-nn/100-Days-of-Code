import tkinter as tk

window = tk.Tk()
window.title("My program")
window.minsize(width=500. height=500)

# Label
my_label = tk.Label(text="Label", font=("Arial", 24, "bold"))
#my_label.pack(expand=True)
my_label.pack(side="left")
my_label["text"] = "New text"
my_label.config(text="New text")

# Button
def button_clicked():
  print("I got clicked")
  my_label.config(text="Button got clicked")
  
button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()
input.get()

window.mainloop()
