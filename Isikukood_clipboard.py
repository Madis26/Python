#Spikker: https://s1n4.wordpress.com/2011/06/23/copy-string-to-clipboard-in-python/

from tkinter import Tk
import Isikukood


root = Tk()
root.withdraw()
root.clipboard_clear()
root.clipboard_append(Isikukood.isik())
root.mainloop()
