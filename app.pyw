from sys import executable
import tkinter as tk
import os, subprocess
from tkinter import Canvas, Frame, Label, font, filedialog


class MyCtr(tk.Tk):
    '''
    MyCtr Creates a TKinter Window that allows to open and close multiple programs at once.
    '''

    def __init__(self):
        super().__init__( )
        self.title("Open and Close Multiple Applications")
        self.applications = []
        self.md_font = font.Font(size=12, family='Helvetica', weight='bold') 

        self.canvas = Canvas(self, height=600, width=900, bg='#012828', bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.frame = Frame(self.canvas, bg='white')
        self.frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

        # Check for saved applications
        if os.path.isfile('save.txt'):
            with open('save.txt') as file:
                tempApps = file.read()
                self.applications = tempApps.split(',')
            self.applications = list(set([app for app in self.applications if app.strip()]))
            for app in self.applications:
                label = Label(self.frame, text=app, padx=10, pady=5)
                label['font'] = self.md_font
                label.pack(fill='both')

    # Create and add usefull bottons to the GUI
    def addButtons(self):    
        fileOpen = tk.Button(self, padx=8, pady=4, text='Open Programs', fg='white', bg='#012828', command=self.openFile)
        fileOpen['font'] = self.md_font
        fileOpen.place(x=0, y=0, relx=0.25, rely=0.86)

        fileRun = tk.Button(self, padx=8, pady=4, text='Run Programs', fg='white', bg='#012828', command=self.runFile)
        fileRun['font'] = self.md_font
        fileRun.place(x=0, y=0, relx=0.6, rely=0.86)

        fileClear = tk.Button(self, padx=8, pady=4, text='Clear Programs', fg='white', bg='#012828', command=self.clearFile)
        fileClear['font'] = self.md_font
        fileClear.pack(fill='both')

        fileStop = tk.Button(self, padx=8, pady=4, text='Stop Programs', fg='#eb3734', bg='#062105', command=self.stopFile)
        fileStop['font'] = self.md_font
        fileStop.place(x=0, y=0, relx=0.1, rely=0.03)

    def openFile(self):
        '''
        Function that opens desktop file explorer and opens program
        '''
        for widget in self.frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir='C:\Program Files', title='Choose Fle', 
        filetypes=( ('executables', '*.exe'), ('all files', '*.*') ))
        
        self.applications.append(filename)
        self.applications = list(set(self.applications))

        for app in self.applications:
            label = Label(self.frame, text=app, padx=10, pady=5)
            label['font'] = self.md_font
            label.pack(fill='both')


    def runFile(self):
        '''
        Funtion that runs executable files
        '''
        for app in self.applications:
            os.startfile(app)

    def stopFile(self):
        '''
        Funtion that stops running executable files
        '''
        for app in self.applications:
            dot_splitted = app.split('.')
            slash_splitted = dot_splitted[0].split('/')
            ext = "{}.{}".format(slash_splitted[-1], dot_splitted[1])
            subprocess.call(["taskkill","/IM", ext])

    def clearFile(self):
        '''
        Function to clear current applications
        '''
        self.applications = []
        for widget in self.frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = MyCtr()
    app.addButtons()
    app.mainloop()
    
    with open('save.txt', 'w') as file:
        for app in app.applications:
            file.write(app + ',')
