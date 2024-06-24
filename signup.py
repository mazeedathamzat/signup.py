from tkinter import *
from PIL import ImageTk

signup_window = Tk()
signup_window.title('Sign-up')
signup_window.resizable(False, False)

background = ImageTk.PhotoImage(file = 'bg.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()


frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text="CREATE AN ACCOUNT", font=("Microsoft Yahei  UI Light ", 15, ),bg='white', fg='firebrick1'  )
heading.grid(row=0,column=0,pady=10)

emailLabel=Label(frame,text='Email',font=("Microsoft Yahei  UI Light ", 10, 'bold'),bg='white', fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=("Microsoft Yahei  UI Light ", 10, 'bold'),bg='firebrick', fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

UsernameLabel=Label(frame,text='Username',font=("Microsoft Yahei  UI Light ", 10, 'bold'),bg='white', fg='firebrick1')
UsernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,1))
UsernameEntry=Entry(frame,width=30,font=("Microsoft Yahei  UI Light ", 10, 'bold'), fg='white',bg='firebrick')
UsernameEntry.grid(row=4,column=0,sticky='w',padx=25)

PasswordLabel=Label(frame,text='Password',font=("Microsoft Yahei  UI Light ", 10, 'bold'),bg='white', fg='firebrick1')
PasswordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,2))
PasswordEntry=Entry(frame,width=30,font=("Microsoft Yahei  UI Light ", 10, 'bold'), fg='white',bg='firebrick')
PasswordEntry.grid(row=6,column=0,sticky='w',padx=25)

ConfirmPasswordLabel=Label(frame,text='Confirm Password',font=("Microsoft Yahei  UI Light ", 10, 'bold'),bg='white', fg='firebrick1')
ConfirmPasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,2))
ConfirmPasswordEntry=Entry(frame,width=30,font=("Microsoft Yahei  UI Light ", 10, 'bold'), fg='white',bg='firebrick')
ConfirmPasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

termsandcondition=Checkbutton(frame,text='I agree to terms and conditions',font=('Microsoft Yahei  UI Light',10,'bold'),fg='firebrick1',bg='white'
                              ,activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandcondition.grid(row=9,column=0,sticky='w',pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open sans serif', 16, 'bold'),bd=0,bg='firebrick',fg='white',activebackground='firebrick1',
                    activeforeground='white',width=17,cursor='hand2')
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'),
                     bg='white', fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame, text='Log in', font=('Open Sans', '9', 'bold underline'), bg='white', fg='blue', bd=0, cursor='hand2',
                    activebackground='white', activeforeground='blue')
loginButton.place(x=170,y=383)


signup_window.mainloop()