import tkinter as tk
from start_page import GfnParser
from utilities import get_driver
from interface import GfnParserApp

if __name__ == "__main__":
    root = tk.Tk()
    driver = get_driver()
    gfn_parser = GfnParser(driver)
    GfnParserApp(root, gfn_parser)
    root.mainloop()
    driver.quit()
