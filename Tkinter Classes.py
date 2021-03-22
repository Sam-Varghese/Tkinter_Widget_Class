from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable

class window():
    
    def __init__(self,window_name,title,back_ground,fore_ground):
        
        self.bg=back_ground
        self.fg=fore_ground
        window_name['background']=back_ground
        t1=Label(window_name,text=title,fg=fore_ground,bg=back_ground,font=('georgia',20))
        t1.grid(row=0,column=1)
        
    def label(self,label_name,text_label,row_no,column_no):
        
        label_name['text']=text_label
        label_name['bg']=self.bg
        label_name['fg']=self.fg
        label_name['font']=('georgia',15)
        label_name.grid(row=row_no,column=column_no,padx=10,pady=10)
        
    def entry(self,entry_name,row_no,column_no,bg,fg,text_inserted=''):
        
        entry_name.insert(0,text_inserted)
        entry_name['bg']=bg
        entry_name['fg']=fg
        entry_name['font']=('georgia',15)
        entry_name.grid(row=row_no,column=column_no,padx=10,pady=10)
        
    def combobox(self,box_name,options,row_no,column_no):
        
        box_name['values']=options
        box_name['state']='readonly'
        box_name['font']=('georgia',15)
        box_name.grid(row=row_no,column=column_no,padx=10,pady=10)
        
win=Tk()
gui=window(win,'Paul Classes','cyan','blue')

l1=Label(win)
gui.label(l1,'Please enter your name: ',1,0)

e1=Entry(win)
gui.entry(e1,1,1,'snow','red','Please do entry')

b1=ttk.Combobox(win)
gui.combobox(b1,['Sam','Angel','Rahul','Arjun'],1,2)

win.mainloop()