from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

window=Tk()
window.title("Send Mail")
window.geometry('500x315')
window.configure(bg='yellow')
window.resizable(False,False)

def cancel():
    sender_email.delete(0,END)
    sender_password.delete(0,END)
    receiver_email.delete(0,END)
    subject.delete('1.0',END)
    message.delete('1.0',END)


def send():
    sender = sender_email.get()
    password = sender_password.get()
    receiver = receiver_email.get()
    global subject
    subject = subject.get('1.0', END)
    global message
    message = message.get('1.0', END)
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)

        server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print("Error:", str(e))

    finally:
        server.quit()





def about():
    messagebox.showinfo("About","about")
menubar=Menu(window)
menubar.add_command(label='About',command=about)
window.config(menu=menubar)

sender_e=Label(window,text='Sender\'s email : ',bg='yellow')
sender_e.grid(row=0,column=0,padx=5,pady=5)
sender_email=Entry(window,bd=3,width=40)
sender_email.grid(row=0,column=1,pady=5)

sender_p=Label(window,text='Sender\'s password : ',bg='yellow')
sender_p.grid(row=1,column=0)
sender_password=Entry(window,bd=3)
sender_password.grid(row=1,column=1,pady=5)

receiver_e=Label(window,text='Receiver\'s email : ',bg='yellow')
receiver_e.grid(row=3,column=0,padx=5)
receiver_email=Entry(window,bd=3,width=40)
receiver_email.grid(row=3,column=1,pady=5)

subjectLabel=Label(window,text='Subject : ',bg='yellow')
subjectLabel.grid(row=4,column=0,padx=5)
subject=Text(window,bd=3,width=40,height=1)
subject.grid(row=4,column=1,pady=5)


messageLabel=Label(window,text="Message : ",bg='yellow')
messageLabel.grid(row=5,column=0,padx=8)
message=Text(window,bd=3,width=40,height=7)
message.grid(row=5,column=1,pady=5)

send=Button(window,text='Send',bg='green',command=send)
send.grid(row=6,column=1)

cancel=Button(window,text='Cancel',command=cancel,bg='red')
cancel.grid(row=6,column=0)


window.mainloop()