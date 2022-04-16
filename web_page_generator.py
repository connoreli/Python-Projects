from tkinter import *
import tkinter as tk
import webbrowser

text = '''
<html>
    <body>
        <h1>Stay tuned for a summer sale!</h1>
    </body>
</html>
'''

file = open("web_page_generator.html","w")
file.write(text)
file.close()

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.config(bg='lightgray')

        self.varBody = StringVar()

        self.txt_body = Entry(self.master, text='')
        self.txt_body.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

    def submit(self):
        customText = self.txt_body.get()
        html_file = open('web_page_generator.html', 'w')
        html_format = "<html>\n<body>\n<p>" + customText + "</p>\n</body>\n</html>"
        html_file.write(html_format)
        html_file.close()
        webbrowser.open_new_tab('web_page_generator.html')


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root = mainloop()
