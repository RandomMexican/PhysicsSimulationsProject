import tkinter as tk

# create window OBJ
window = tk.Tk()

def handle_click(event):
    """
        should send you to the sim you clicked on
        for now just print `clicked`
    """
    print("clicked")


for i in range(1):
    # window.columnconfigure(i,weight=1, minsize=75)
    # window.rowconfigure(i,weight=1,minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master= window,
            relief= tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master= frame, text=f"Row {i} \nComun {j}")
        label.pack()

# run the tinker event loop 
window.mainloop()