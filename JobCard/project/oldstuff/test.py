import tkinter as tk
import matplotlib
# import urllib
# import json
# import matplotlib.animation as animation
# import matplotlib.dates as mdates
# import matplotlib.ticker as mticker
# import pandas as pd
# import numpy as np

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from tkinter import ttk
from matplotlib import style
# from matplotlib import pyplot as plt
# from matplotlib.figure import Figure

matplotlib.use("TkAgg")

LARGE_FONT = ("Verdana", 12)

style.use("ggplot")


# f = plt.figure()

# Creating the main window
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea Of BTC client")
        # tk.Tk.iconbitmap(self, default="gbl.ico")
        #
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # for F in(StartPage, PageOne, PageTwo):
        #         frame = F(container, self)
        #         self.frames[F] = frame
        #         frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Load the StartPage in Main App
# plus create the start page
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Visit Page 1",
#                             command=lambda: controller.show_frame(PageOne))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Visit Page 2",
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page One", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Back to Home!",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Page Two",
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page Two", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Back to Home!",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Page One",
#                             command=lambda: controller.show_frame(PageOne))
#         button2.pack()


app = SeaofBTCapp()
app.geometry("280x250+180+80")
app.mainloop()


