# import tkinter as tk

# # create a window Obj
# window = tk.Tk()

# #assume this gets auto updated
# events = []

# #create event handler
# def handle_keypress(event):
#     """
#         print the character associated with the key pressed
#     """
#     print(event.char)

# window.bind("<Key>",handle_keypress)

# #run event loop
# window.mainloop()

# #Event loop
# while True:
#     #  if the event list is empty then no events have occurred 
#     # and you can skip to the next iteration of the loop
    
#     if events == []:
#         continue
    
#     #  if the while loop reaches this point it means theres at least one event
#     #  object in the event list
#     event = events[0]

#     # if the event is a keypress event obj
#     if event.type == "keypress":
#         # call the event handler
#         handle_keypress(event)



#     button = tk.Button(
#         text="Click",
#         width=10,
#         height=5,
#         bg="black",
#         fg= "white"
#         )
#     button.bind("<Button>", handle_keypress)

#     for i in range(3):
#         window.columnconfigure(i,weight=1,minsize=75)
#         window.rowconfigure(1,weight=1,minsize=50)
#         for j in range(3):
#             frame = tk.Frame(
#                 master=window,
#                 relief=tk.RAISED,
#                 borderwidth=1
#             )
#             frame.grid(row=i, column=j, padx=5 ,pady=5)
#             label = tk.Label(master=frame, text= f"Row {i} /nColumn {j}")
#             label.pack(padx=5,pady=5)

#     button.pack()

# # window.mainloop()




**********************************************************************************************************************

import tkinter as tk

#create a window OBJ
window = tk.Tk()

events = []

for i in range(3):
    window.columnconfigure(i, weight=1 , minsize= 75)
    window.rowconfigure(1,weight=1,minsize=50)
    for l in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=i, padx=5, pady=5)
        button = tk.Button(
            text="Click",
            width=10,
            height=5,
            bg="black",
            fg="white"
        )
        

window.mainloop()


