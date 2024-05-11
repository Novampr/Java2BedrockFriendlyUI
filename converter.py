import TKinterModernThemes as TKMT
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import ctypes as ct
import os

def buttonCMD():
        print("Button clicked!")

class App(TKMT.ThemedTKinterFrame):
        def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
                super().__init__("J2B GUI", theme, mode, usecommandlineargs, usethemeconfigfile)

                self.root.resizable(False, False)
                self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAAKAAAACgCAYAAACLz2ctAAAEXElEQVR4Ae3BsY3jShBF0TsFme0whUUHIGBaPrPYAKRsNgXmMvJFgwFUDnToz0+hjAbeN945X8/n85eC4zj4P+u9U7GuKxX7vlNxXRcV67pS8X6/qchMZuq9U5GZVPTeqQjMhAIzocBMKDATCsyEAjOhwEwoMBMKzIRux3FQcb/fmWmMQcW+71SMMajY952KMQYV27ZRsa4rFeu6UtFao+Ln54eKzKSi905FZlIRmAkFZkKBmVBgJhSYCQVmQoGZUGAmFJgJfX1/f/9ScJ4nFcuyMNN5nlQsy4LC6/WiYts2KnrvKKzrSsX7/aaitUZFYCYUmAkFZkKBmVBgJhSYCQVmQoGZUGAmdOu9U7GuKxX7vjPTdV1UfD4fKh6PBxXrulLxfr+p6L1TkZkoZCYz9d6pCMyEAjOhwEwoMBMKzIQCM6HATCgwEwrMhG6fz4eKzKTi9XpRsW0bMy3LQkVmMlNmMtP9fqdijMFM+74z03EcVARmQoGZUGAmFJgJBWZCgZlQYCYUmAkFZkJf39/fvxT03lHITCp678yUmcx0nicVj8eDmTKTmc7zpGJZFioCM6HATCgwEwrMhAIzocBMKDATCsyEAjOh2+v1YqZ936m4rouK+/1OxRiDmVprVFzXRUVrjYoxBjO11qgYY1CxbRsV53lSEZgJBWZCgZlQYCYUmAkFZkKBmVBgJhSYCX39/fv3F4HMpKL3jkJmMtN5nlQsy8JMvXcqMpOK+/1OxXVdVARmQoGZUGAmFJgJBWZCgZlQYCYUmAkFZkK31hoVYwwUMpOZeu9U9N6paK1RMcZgpn3fqRhjULGuKwqBmVBgJhSYCQVmQoGZUGAmFJgJBWZCgZnQ7bouKrZtY6bzPKlYloWK3jsVmUlF752K4ziY6bouKjKTiuM4mOn1elGx7zsVgZlQYCYUmAkFZkKBmVBgJhSYCQVmQoGZ0Nfz+fxlojEGFdu2UXG/36kYYzDTtm1UnOdJxbIsVLxeLxT2fafiOA5mCsyEAjOhwEwoMBMKzIQCM6HATCgwEwrMhL7+/PnzS8Hj8UAhM5mp905Fa42KMQYzvd9vKlprzDTGYKZ///5REZgJBWZCgZlQYCYUmAkFZkKBmVBgJhSYCd0ejwcVmYnC/X6n4rouKjIThTEGFZmJwnEczPR4PKgIzIQCM6HATCgwEwrMhAIzocBMKDATCsyEbq01Kl6vFxX7vlMxxqDi/X5T8fl8qHg8HlRkJhXHcVBxHAcV53lSsSwLFb13KlprVIwxmCkwEwrMhAIzocBMKDATCsyEAjOhwEwoMBP6ej6fv0x0XRcVmclMvXcqMpOZeu9UtNaoGGMw0/v9piIzman3TkVgJhSYCQVmQoGZUGAmFJgJBWZCgZlQYCZ0O46DivM8qViWhZnO86RiXVcq1nWlYt93Ko7joKL3TsW+71T8/PxQsSwLM/XeqWitURGYCQVmQoGZUGAmFJgJBWZCgZlQYCYUmAn9B6DfFyk43rwUAAAAAElFTkSuQmCC"))

                try:
                    self.root.update()
                    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
                    get_parent = ct.windll.user32.GetParent
                    hwnd = get_parent(self.root.winfo_id())
                    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
                    value = 2
                    value = ct.c_int(value)
                    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
                except:
                    pass

                self.Text("Java2Bedrock Converter GUI", padx=10, pady=10, fontargs=("Ariel", 28, "bold"))
                self.frame = self.addLabelFrame("Input Parameters")
                style = ttk.Style()
                style.configure("BW.TEntry", padding=5)
                style.configure("BW.TButton", padding=10)

                javaPath = ttk.Label(self.frame.master, text="Java Resource Pack Path", font=("Ariel", 14, "bold"))
                javaPath.pack()

                t = StringVar()
                text = ttk.Entry(self.frame.master, width=65, name="value", textvariable=t, style="BW.TEntry")
                text.pack()

                def getFile():
                    t.set(askopenfilename(
                        title="Select ZIP file...",
                        filetypes=[("ZIP files", "*.zip")]
                    ))

                browse = ttk.Button(self.frame.master, text="Browse", command=getFile, style="BW.TButton")
                browse.pack()

                def convert():
                    os.system("./converter.sh \""+t.get()+"\" -w \"false\" -m \"null\" -a \"entity_alphatest_one_sided\" -b \"alpha_test\" -f \"null\" -v \"1.20.4\" -u \"true\"")

                execute = ttk.Button(self.frame.master, text="Convert", command=convert, style="BW.TButton")
                execute.pack()

                self.run()


if __name__ == "__main__":
        App("sun-valley", "dark")