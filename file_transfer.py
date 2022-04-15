import shutil
import os

#set where the source of the files are
source = 'C:/Users/conno/OneDrive/Documents/GitHub/Python-Projects/Folder A'

#set the destination path to folder B
destination = 'C:/Users/conno/OneDrive/Documents/GitHub/Python-Projects/Folder B'
files = os.listdir(source)

for i in files:
    #we are saying move the files represnted by 'i' to their new destination
    shutil.move(source+i, destination)



class file(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("File Transfer")
        self.button1 = Button(self, text = "BROWSE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = file2()
class file2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    file().mainloop()
if __name__ == '__main__':
    main()
