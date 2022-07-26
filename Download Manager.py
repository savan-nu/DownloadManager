import json
import urllib
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import requests
import urllib.request
from fpdf import FPDF
import os

root = Tk()
root.title("Download Manager")
hei = 700
wi = 1300
root.geometry(f"{wi}x{hei}")
root.maxsize(wi, hei)
root.minsize(wi, hei)
home = Frame(root, height=700, width=1300)
home.pack()
logi = PhotoImage(file=r"Home_page.png")
after_login = PhotoImage(file=r"after_login.png")
youtube_button = PhotoImage(file=r"Youtube_button.png")
File_button = PhotoImage(file=r"File_button.png")
You_tube_dow = PhotoImage(file=r"Dwnload_youtube.png")
photo = PhotoImage(file=r"File_download.png")
account = PhotoImage(file=r"account_details.png")

Folder_Name = ""


def extra_video():
    ch = numberChosen.get()
    urll = yflie.get()
    if (len(urll) > 1):
        s = ""
        params = {"format": "json", "url": urll}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            # pprint.pprint(data)
            s = data['title']

        with open(f'{u_name.get()}.txt', 'a+') as f:
            st = f.read()
            f.write(s + "    ")
            f.write(urll + "\n")

        yt = YouTube(urll)

        if (ch == qua[0]):
            select = yt.streams.filter(progressive=True).first()

        elif ch == qua[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif ch == qua[2]:
            select = yt.streams.filter(only_audio=True).first()

    select.download(Folder_Name)
    # com.config(text = "Download Completed" ,fg = "green" ,font="{Fira Code} 12 bold")


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        # print(Folder_Name)
        LocationError.config(text=Folder_Name, fg="green")
    else:
        LocationError.config(text="No file Selected", fg="red")


def log_in_in_home():
    with open("account_details.txt", 'r+') as f:
        string1 = f.read()

    # print(string1)
    p = string1.split('\n')
    l = []
    # print(l)
    l_final = ""
    for i in p:
        if i == '':
            continue
        else:
            l.append(i)


    f = False
    for i in range(0, len(l), 2):
        if l[i] == u_name.get():
            if l[i + 1] == passw.get():
                f = True
            else:
                f = False
                break

    if f:
        Label(text="Login success......",fg="#4b4647", bg="white", border=0, font=("Book Antiqua", 20, 'bold')).place(x=750, y=530, height=28,width=434)
        after_login_fun()
    else:
        Label(text="Please signup first.......",fg="#4b4647", bg="white", border=0, font=("Book Antiqua", 20, 'bold')).place(x=750, y=530, height=28,width=434)



def sign_up_home():

    with open("account_details.txt", 'r+') as f:
        string1 = f.read()

        # print(string1)
    p = string1.split('\n')
    l = []
    # print(l)
    l_final = ""
    for i in p:
        if i == '':
            continue
        else:
            l.append(i)


    f = True
    for i in range(0,len(l),2) :
        if l[i] == u_name.get():
            Label(text='User Already Exits', fg="#4b4647", bg="white", border=0,
                  font=("Book Antiqua", 20, 'bold')).place(x=750, y=530, height=28, width=434)

            f = False

    if f :
        with open("account_details.txt", "a+") as f:
            f.write(u_name.get() + '\n')
            f.write(passw.get() + '\n')

        Label(text="Your Sign Up is commpleted", fg="#4b4647", bg="white", border=0,
              font=("Book Antiqua", 20, 'bold')).place(x=750, y=530, height=28, width=434)
        with open(f'{u_name.get()}.txt', 'a') as f1:
            f1.write(f"\t\t\t\t\t{u_name.get()}'s History\n")

        after_login_fun()


def changePassword():
    u_n = u_name.get()
    paw =  new_password.get()
    with open("account_details.txt", "r+") as f:
        s = f.read()

    l = s.split('\n')
    for i in range(0, len(l), 2):
        if l[i] == u_n:
            l[i + 1] = paw
            break

    with open("account_details.txt", "w") as f:
        for i in l:
            f.write(i + '\n')

    print("Password is Changed :")


def delete_account() :
    u_n = u_name.get()
    if os.path.exists(f'{u_n}.txt'):
        os.remove(f'{u_n}.txt')

    if os.path.exists(f'{u_n}.pdf') :
        os.remove(f'{u_n}.pdf')

    with open("account_details.txt", "r") as f:
        s = f.read()

    p = s.split('\n')
    l = []
    # print(l)
    l_final = ""
    for i in p :
        if i == '' :
            continue
        else :
            l.append(i)


    # print(l)
    for i in range(0, len(l), 2):
        # print(l[i] + " " + str(i))
        if l[i] == u_n:
            continue
        else :
            l_final += l[i] + '\n' + l[i+1] + '\n'


    # print(l_final)
    with open("account_details.txt", "w") as f:
        f.write(l_final)

    print("Deleted...")

    home_page()

def dow_pdf ():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=9)

    f = open(f'{u_name.get()}.txt', 'r')
    for i in f:
        pdf.cell(200, 10, txt=i, ln=2, align='c')

    pdf.output(f'{u_name.get()}.pdf')


def My_account():
    for widget in home.winfo_children():
        widget.destroy()

    Label(image=account).place(x=0, y=0, height=700, width=1300)
    Label(text=u_name.get(),fg="#4b4647", bg="white", border=0, font=("Book Antiqua", 20, 'bold')).place(x=422, y=283, height=28,width=434)
    global new_password
    new_password= StringVar()
    global chane_password
    change_password = Entry(bg="white",textvariable=new_password,border=0, font=("Book Antiqua", 12, 'bold'),show='*')
    change_password.place(x=421,y=353,height = 28, width = 434)
    Button(text="SAVE",fg="#4b4647",font=("Copperplate Gothic Bold", 14),bg="white",border=0,command=changePassword).place(x=700,y=392,height=22,width=95)
    Button(text="HISTORY",fg="#4b4647",font=("Copperplate Gothic Bold", 22),bg="white",border=0,command=dow_pdf).place(x=534,y=435,height=36,width=209)
    Button(text="DELETE ACCOUNT",fg="#4b4647",font=("Copperplate Gothic Bold", 22),bg="white",border=0,command = delete_account).place(x=487,y=501,height=44,width=322)
    Button(text="BACK",fg="#4b4647",font=("Copperplate Gothic Bold", 18),bg="white",border=0 ,command=after_login_fun).place(x=603,y=597,height=24,width=90)


def after_login_fun():
    uname = u_name.get()
    pass_w = passw.get()
    for widget in home.winfo_children():
        widget.destroy()
    Label(image=after_login).place(x=0, y=0, height=700, width=1300)
    Button(image=youtube_button, relief="flat", command=You_tube_dow_fun).place(x=156, y=251, width=322, height=57)
    Button(image=File_button, relief="flat", command=file_download_fun).place(x=837, y=251, width=322, height=57)

    Button(text="BACK", font=("Book Antiqua", 25, 'bold'), fg='#353030', bg='white', relief="flat",
           command=home_page).place(x=354, y=608, width=225, height=40)
    Button(text="MY ACCOUNT", font=("Book Antiqua", 25, 'bold'), relief="flat", bg='white', fg='#353030',
           command=My_account).place(x=726, y=608, width=250, height=40)


def You_tube_dow_fun():
    for widget in home.winfo_children():
        widget.destroy()
    Label(image=You_tube_dow).place(x=0, y=0, height=700, width=1300)
    global yflie
    global link
    link = StringVar()
    global yflie
    yflie = Entry(width=40, bg="white", border=0, textvariable=link, fg="#7D0541", font=("Book Antiqua", 25, 'bold'))
    yflie.place(x=404, y=252, height=45, width=500)
    Button(bg="#ffffff", fg="#ae171a", border=0, text="Choose Location", font=("Book Antiqua", 25, 'bold'),
           command=openLocation).place(x=476, y=305, height=33, width=350)
    global LocationError
    LocationError = Label(bg="#ffffff", fg="#ae171a", border=0, text="YOUR PATH IS HERE",
                          font=("Book Antiqua", 22, 'bold'))
    LocationError.place(x=406, y=352, height=36, width=475)
    global qua
    qua = ["720p", "144p", "Audio Only"]
    number = StringVar()
    global numberChosen
    numberChosen = ttk.Combobox(font=("Book Antiqua", 12, 'bold'), width=12, textvariable=number)
    numberChosen['values'] = ("720p", "144p", "Audio Only")
    numberChosen.place(x=413, y=456, height=37, width=304)
    Button(bg="#ffffff", fg="#ae171a", text="BACK", border=0, font=("Book Antiqua", 19, 'bold'),
           command=after_login_fun).place(x=475, y=545, height=28, width=134)
    Button(bg="#ffffff", fg="#ae171a", text="DOWNLOAD", border=0, font=("Book Antiqua", 19, 'bold'),
           command=extra_video).place(x=657, y=545, height=28, width=230)


def home_page():
    for widget in home.winfo_children():
        widget.destroy()
    Label(image=logi).place(x=0, y=0, height=700, width=1300)
    global u_name
    u_name = StringVar()
    global u_entry
    u_entry = Entry(textvariable=u_name, bg="white", border=0, font=('book antiqua', 18, 'bold'), fg="#7D0541")
    u_entry.place(x=890, y=302, width=252, height=42)
    global passw
    passw = StringVar()
    passw_entry = Entry(textvariable=passw, bg="white", border=0, font=('book antiqua', 18, 'bold'), fg="#7D0541",show='*')
    passw_entry.place(x=890, y=383, width=252, height=42)
    Button(bg="white", text="SIGN UP", font=({'copperplate gothic'}, 14, 'bold'), fg='#c91a19', border=0,
           command=sign_up_home).place(x=892, y=465, height=40, width=105)
    Button(bg="white", text="LOG IN", font=({'copperplate gothic'}, 14, 'bold'), fg='#c91a19', border=0,
           command=log_in_in_home).place(x=1034,
                                         y=465,
                                         height=40,
                                         width=105)


def file_download_fun():
    Label(image=photo).place(x=0, y=0, height=700, width=1300)
    global ur
    ur = StringVar()
    global urlentry
    urlentry = Entry(root, textvariable=ur, bg="#d55858", font=('book antiqua', 10))
    urlentry.place(x=33, y=95, height=35,width=480)
    print(ur.get())

    Button(root, width=10, bg="#d55858", fg="#4a4242", text="Choose Path", command=Location,
           font=('book antique', 20, 'bold'), borderwidth=3, relief=SUNKEN).place(x=80, y=140, height=40,
                                                                                  width=400)

    global locationErr
    locationErr = Label(root, text="Your path is here", bg="#d55858", fg="#4a4242",
                        font=('book antiqua', 20, 'bold'))
    locationErr.place(x=33, y=190, height=40, width=500)

    global f_entry
    global f_name
    f_name = StringVar()
    f_entry = Entry(root, textvariable=f_name, bg="#d55858", font=('book antiqua', 20))
    f_entry.place(x=33, y=288, height=35,width=480)

    Button(root, width=10, bg="#d55858", fg="#4a4242", text="DOWNLOAD", command=download_file,
           font=('book antique', 20, 'bold')).place(x=80, y=341, height=40, width=400)
    li = f_entry.get()

    Button(root, width=10, bg="#d55858", fg="#4a4242", text="BACK", command=after_login_fun,
           font=('book antiqua', 20, 'bold')).place(
        x=190, y=576, height=40, width=150)


def download_file():
    try:
        filename = f_name.get()
        req = requests.get(ur.get())
        url = ur.get()

        if filename:
            pass
        else:
            filename = req.url[url.rfind('/') + 1:]

        filename = Folder_Name + "\\" + filename
        with requests.get(url) as re:
            with open(filename, 'wb') as f:
                for chunk in re.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            li = f_entry.get()
            with open(f'{u_name.get()}.txt', "a+") as f1:
                f1.write(li+"   ")
                li = urlentry.get()
                f1.write(li + "\n")

            return filename
    except Exception as e:
        print(e)
        return None



def Location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationErr.config(text=Folder_Name, fg="green")
    else:
        locationErr.config(text="Please Choose Folder!!", fg="red")


# downloadUrl = 'https://omextemplates.content.office.net/support/templates/en-us/tf16402488.dotx'


home_page()
root.mainloop()