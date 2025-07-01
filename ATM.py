import tkinter as tk
import time


current_balance=1000


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.shared_data={'Balance':tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name= F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame("StartPage")
    
    def show_frame(self,page_name):
        frame= self.frames[page_name]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#003399')
        self.controller=controller
        self.controller.title('ATM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/atm_icon.png'))
        
        heading_label=tk.Label(self,
                              text='Monster baNk',font=('Monster AG',50,'bold'),
                              foreground='white',
                              background='#003399')
        heading_label.pack(pady=25)
        
        space_Label=tk.Label(self,height=4,bg='#003399')
        space_Label.pack()
        
        password_Label=tk.Label(self,
                              text='enter your password',font=('Monster AG',16),
                              foreground='white',
                              background='#003399')
        password_Label.pack(pady=10)
        
        my_password=tk.StringVar()
        password_entry_box=tk.Entry(self,textvariable= my_password,
                                    font=('Monster AG',14),
                                    width=41)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)
        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
        password_entry_box.bind('<FocusIn>',handle_focus_in)
        
        def check_password():
         if my_password.get() =='0000':
            my_password.set('')
            incorrect_password_label['text']=''
            controller.show_frame('MenuPage')
         else:
            incorrect_password_label['text']='IncOrrect PasswOrd'
            
        enter_button=tk.Button(self,
                               text='Enter',command=check_password,
                               relief='raised',
                               borderwidth=3,
                               width=44,height=3)
        enter_button.pack(pady=20)
        
        incorrect_password_label=tk.Label(self,
                                          text='',
                                          font=('Monster AG',16),
                                          fg='red',
                                          bg='#002266',
                                          anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
        visa_photo = tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
        
        mastercard_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo
        
        jcb_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/jcb.png')
        jcb_label=tk.Label(bottom_frame,image=jcb_photo)
        jcb_label.pack(side='left')
        jcb_label.image=jcb_photo
        def tick():
            current_time=time.strftime('%Y/%m/%d   %I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label=tk.Label(bottom_frame,font=('Monster AG',12))
        time_label.pack(side='right')
        tick()
class MenuPage(tk.Frame):
    def __init__(self,parent,controller):   
        tk.Frame.__init__(self,parent,bg='#003399')   
        self.controller=controller
        
        heading_label=tk.Label(self,
                              text='Monster baNk',font=('Monster AG',50,'bold'),
                              foreground='white',
                              background='#003399')
        heading_label.pack(pady=25)
        
        main_menu_label=tk.Label(self,
                                 text='Main Menu',font=('Monster AG',20),
                                 foreground='white',
                                 background='#003399')
        main_menu_label.pack()
        
        selection_label=tk.Label(self,
                                 text='Please make a selection',font=('Monster AG',18),
                                 foreground='white',
                                 background='#003399',
                                 anchor='w')
        selection_label.pack(fill='x')
        
        
        button_frame=tk.Frame(self,bg='#002b80')
        button_frame.pack(fill='both',expand=True)
        
        def withdraw():
            controller.show_frame('WithdrawPage')
        withdraw_button=tk.Button(button_frame,text='Withdraw',
                                  command=withdraw,
                                  relief='raised',
                                  borderwidth=3,
                                  width=40,
                                  height=4)
        #withdraw_button.grid(column=0,row=0,pady=5)
        withdraw_button.pack(side='top',pady=10)

        def deposit():
            controller.show_frame('DepositPage')
        deposit_button=tk.Button(button_frame,text='Deposit',
                                  command=deposit,
                                  relief='raised',
                                  borderwidth=3,
                                  width=40,
                                  height=4)
        #deposit_button.grid(column=0,row=1,pady=5)
        deposit_button.pack(side='top',pady=10) 

        def balance():
            controller.show_frame('BalancePage')
        balance_button=tk.Button(button_frame,text='Balance',
                                  command=balance,
                                  relief='raised',
                                  borderwidth=3,
                                  width=40,
                                  height=4)
        #balance_button.grid(column=0,row=2,pady=5)
        balance_button.pack(side='top',pady=10)  

        def exit():
            #controller.show_frame('StartPage')
            self.controller.destroy()
        exit_button=tk.Button(button_frame,text='Exit',
                                  command=exit,
                                  relief='raised',
                                  borderwidth=3,
                                  width=40,
                                  height=4)
        #exit_button.grid(column=0,row=3,pady=5)
        exit_button.pack(side='top',pady=10)                                       
                                        
        
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
        visa_photo = tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
        
        mastercard_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo
        
        jcb_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/jcb.png')
        jcb_label=tk.Label(bottom_frame,image=jcb_photo)
        jcb_label.pack(side='left')
        jcb_label.image=jcb_photo
        def tick():
            current_time=time.strftime('%Y/%m/%d   %I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label=tk.Label(bottom_frame,font=('Monster AG',12))
        time_label.pack(side='right')
        tick()
class WithdrawPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#003399')   
        self.controller=controller
        
        heading_label=tk.Label(self,
                              text='Monster baNk',font=('Monster AG',50,'bold'),
                              foreground='white',
                              background='#003399')
        heading_label.pack(pady=25)
        
        choose_amount_label=tk.Label(self,
                                 text='choose the amount you want to withdraw',font=('Monster AG',18),
                                 foreground='white',
                                 background='#003399',
                                 anchor='w')
        choose_amount_label.pack()
        
        
        button_frame=tk.Frame(self,bg='#002b80')
        button_frame.pack(fill='both',expand=True)
        
        def withdraw(amount):
            global current_balance
            #current_balance-=amount
            #controller.shared_data['Balance'].set(current_balance)
            #no_money_label['text']=''
            #controller.show_frame('MenuPage')
            
            if  amount > current_balance :
                no_money_label['text']='No enough money to withdraw'
                cash.set('')    
                
            else:
                no_money_label['text']=''
                current_balance-=amount
                controller.shared_data['Balance'].set(current_balance)
                cash.set('')
                controller.show_frame('MenuPage')   
                
        twenty_button=tk.Button(button_frame,text='20',font=('Monster AG',12),
                                       command=lambda:withdraw(20),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        twenty_button.grid(column=0,row=0,pady=5,padx=50)
        
        forty_button=tk.Button(button_frame,text='40',font=('Monster AG',12),
                                       command=lambda:withdraw(40),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        forty_button.grid(column=0,row=1,pady=5)
        
        sixty_button=tk.Button(button_frame,text='60',font=('Monster AG',12),
                                       command=lambda:withdraw(60),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        sixty_button.grid(column=0,row=2,pady=5)
        
        eighty_button=tk.Button(button_frame,text='80',font=('Monster AG',12),
                                       command=lambda:withdraw(80),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        eighty_button.grid(column=0,row=3,pady=5)
        
        one_hundred_button=tk.Button(button_frame,text='100',font=('Monster AG',12),
                                       command=lambda:withdraw(100),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        one_hundred_button.grid(column=1,row=0,pady=5,padx=325)
        
        two_hundred_button=tk.Button(button_frame,text='200',font=('Monster AG',12),
                                       command=lambda:withdraw(200),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        two_hundred_button.grid(column=1,row=1,pady=5)
        
        three_hundred_button=tk.Button(button_frame,text='300',font=('Monster AG',12),
                                       command=lambda:withdraw(300),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        three_hundred_button.grid(column=1,row=2,pady=5)
        
        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('Monster AG',11),
                                    textvariable=cash,
                                    width=58,
                                    justify='center',
                                    relief='raised',
                                    bd=3)
        other_amount_entry.grid(column=1,row=3,pady=5,ipady=30)
        
        def other_amount(_):
            global current_balance
            if int(cash.get()) > current_balance :
                no_money_label['text']='No enough money to withdraw'
                cash.set('')
            else:
                no_money_label['text']=''
                current_balance-=int(cash.get())
                controller.shared_data['Balance'].set(current_balance)
                cash.set('')
                controller.show_frame('MenuPage')   
        other_amount_entry.bind('<Return>',other_amount)
        
        no_money_label=tk.Label(self,
                                text='',font=('Monster AG',20),
                                foreground='red',
                                background='#002b80',
                                anchor='e')
        no_money_label.pack(fill='x')
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
        visa_photo = tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
        
        mastercard_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo
        
        jcb_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/jcb.png')
        jcb_label=tk.Label(bottom_frame,image=jcb_photo)
        jcb_label.pack(side='left')
        jcb_label.image=jcb_photo
        def tick():
            current_time=time.strftime('%Y/%m/%d   %I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label=tk.Label(bottom_frame,font=('Monster AG',12))
        time_label.pack(side='right')
        tick()
class DepositPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#003399')   
        self.controller=controller
        
        heading_label=tk.Label(self,
                              text='Monster baNk',font=('Monster AG',50,'bold'),
                              foreground='white',
                              background='#003399')
        heading_label.pack(pady=25)
        
        space_Label=tk.Label(self,height=4,bg='#003399')
        space_Label.pack()
        
        enter_amount_Label=tk.Label(self,
                              text='Enter your deposit amount',font=('Monster AG',16),
                              foreground='white',
                              background='#003399')
        enter_amount_Label.pack(pady=10)
        
        cash = tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,
                               font=('Monster AG',12),
                               width=41)
        deposit_entry.pack(ipady=7)
        
        def deposit_cash():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
            
        enter_button=tk.Button(self,
                               text='Enter',command=deposit_cash,
                               relief='raised',
                               borderwidth=3,
                               width=40,height=3)
        enter_button.pack(pady=20)
        
        two_tone_label=tk.Label(self,bg='#002b80')
        two_tone_label.pack(fill='both',expand=True)
        
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
        visa_photo = tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
        
        mastercard_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo
        
        jcb_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/jcb.png')
        jcb_label=tk.Label(bottom_frame,image=jcb_photo)
        jcb_label.pack(side='left')
        jcb_label.image=jcb_photo
        def tick():
            current_time=time.strftime('%Y/%m/%d   %I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label=tk.Label(bottom_frame,font=('Monster AG',12))
        time_label.pack(side='right')
        tick()
class BalancePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#003399')   
        self.controller=controller
        heading_label=tk.Label(self,
                              text='Monster baNk',font=('Monster AG',50,'bold'),
                              foreground='white',
                              background='#003399')
        heading_label.pack(pady=25)
        
        space_Label=tk.Label(self,height=4,bg='#003399')
        space_Label.pack()
        
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        current_balance > 0 ;
        balance_label=tk.Label(self,
                               textvariable=controller.shared_data['Balance'],
                               font=('Monster AG',18),fg='white',
                               background='#003399')
        balance_label.pack(fill='x')
        
        buttom_frame=tk.Frame(self,bg='#002b80')
        buttom_frame.pack(fill='both',expand=True)
        
        def menu():
            controller.show_frame('MenuPage')
            
        Menu_button=tk.Button( buttom_frame,
                               text='Menu',command=menu,
                               relief='raised',
                               borderwidth=3,
                               width=40,height=3)
        Menu_button.pack(pady=10)
        
        def exit():
            controller.show_frame('StartPage')
        exit_button=tk.Button(buttom_frame,
                              text='Exit',
                              command=exit,
                              relief='raised',
                              borderwidth=3,
                              width=40,height=3)
        exit_button.pack(pady=10)
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        
        visa_photo = tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
        
        mastercard_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo
        
        jcb_photo=tk.PhotoImage(file='C:/Users/admin/PythonCode/tkinter/ATM/jcb.png')
        jcb_label=tk.Label(bottom_frame,image=jcb_photo)
        jcb_label.pack(side='left')
        jcb_label.image=jcb_photo
        def tick():
            current_time=time.strftime('%Y/%m/%d   %I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
        time_label=tk.Label(bottom_frame,font=('Monster AG',12))
        time_label.pack(side='right')
        tick()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()