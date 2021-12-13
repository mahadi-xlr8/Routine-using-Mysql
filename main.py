from tkinter import *
from tkmacosx import *
from mysql.connector import *
from time import *
import webbrowser as web

mydb = connect(
  host="localhost",
  user="root",
  password="mahadi7118",
  database='project'
)

all_time=ctime().split()
today=all_time[0]
temp=all_time[3].split(":")
time_now=int(temp[0])*60+int(temp[1])
time_now=600


point= mydb.cursor()


point.execute("select * from routine where days Like %s",[today+'%'])
classes=point.fetchall()

class_now={}
class_details=[]
time_slot={}
class_on_going="it's not any class time"


for i in classes:
  stemp=i[6].split(':')
  etemp=i[7].split(":")
  start=int(stemp[0])*60+int(stemp[1])

  end=int(etemp[0])*60+int(etemp[1])
  time_slot[start]=i[3]
  if time_now>=start and time_now<=end:
    class_now[i[3]]=i[8]
    class_details=i
    class_on_going=i[3]

print(class_details)


def open_link():
  web.open(class_now[class_on_going])

def moreInfo():
  return

course_name=''
teacher_name=''
course_code=''
class_start=''
class_end=''

if len(class_details)!=0:
  for i in range(len(class_details)):
    if i==2:
      course_name=class_details[i]
    if i==4:
      teacher_name=class_details[i]
    if i==5:
      course_code=class_details[i]
    if i==6:
      class_start=class_details[i]
    if i==7:
      class_end=class_details[i]











root=Tk();
root.geometry('800x800')
root.configure(bg='#faf598')
root.title("Home")
def details_window():
  nroot=Toplevel(root)
  nroot.title('Class Details')
  nroot.geometry("700x500")
  nroot.configure(bg='#faf598')
  Label(nroot, text="Course Name:", font="Helvetica 30 bold", fg="red",bg='black').grid(row=0, column=0, padx=10, pady=10)
  Label(nroot, text=course_name, font="Helvetica 30 bold", fg="red", bg='black').grid(row=0, column=3, padx=30,pady=10)
  Label(nroot, text="Teacher's Name:", font="Helvetica 30 bold", fg="red",bg='black').grid(row=1, column=0, padx=10, pady=10)
  Label(nroot, text=teacher_name, font="Helvetica 30 bold", fg="red", bg='black').grid(row=1, column=3, padx=30,pady=10)
  Label(nroot, text="Course Code:", font="Helvetica 30 bold", fg="red",bg='black').grid(row=2, column=0, padx=10, pady=10)
  Label(nroot, text=course_code, font="Helvetica 30 bold", fg="red", bg='black').grid(row=2, column=3, padx=30,pady=10)
  Label(nroot, text="Start Time:", font="Helvetica 30 bold", fg="red",bg='black').grid(row=3, column=0, padx=10, pady=10)
  Label(nroot, text=class_start, font="Helvetica 30 bold", fg="red", bg='black').grid(row=3, column=3, padx=30,pady=10)
  Label(nroot, text="End Time:", font="Helvetica 30 bold", fg="red",bg='black').grid(row=4, column=0, padx=10, pady=10)
  Label(nroot, text=class_end, font="Helvetica 30 bold", fg="red", bg='black').grid(row=4, column=3, padx=30,pady=10)


def add_class():
  return;


def update_class():
  return;


def remove_class():
  return;




Label(root,bg='#faefcf').grid(row=0,column=0,columnspan=6)
Label(root,text="Time:",font="Helvetica 40 bold",fg="red").grid(row=1,column=0,padx=10,pady=10)
Label(root,text="10:00",font="Helvetica 40 bold",fg="red").grid(row=1,column=1,padx=10,pady=10)
Label(root,text="11:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=2,padx=10,pady=10)
Label(root,text="1:00",font="Helvetica 40 bold",fg="red").grid(row=1,column=3,padx=10,pady=10)
Label(root,text="2:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=4,padx=10,pady=10)
Label(root,text="Today's class:",font="Helvetica 25 bold",fg="red").grid(row=2,column=0,padx=10,pady=10)

if len(classes)==0:
  Label(root, text="there is no class today!", font="helvetica 25 bold", fg="red").grid(row=2, column=1, padx=10,pady=10, columnspan=3)
else :
  for i in time_slot:
    if i == 600:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=1, padx=10, pady=10)
    elif i == 690:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=2, padx=10, pady=10)
    elif i == 780:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=3, padx=10, pady=10)
    elif i == 870:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=4, padx=10, pady=10)
Label(root,text="Class on going:",font="Helvetica 25 bold",fg="red").grid(row=3,column=0,padx=10,pady=10)
Label(root,text=class_on_going,font="Helvetica 25 bold",fg="red").grid(row=3,column=1,padx=10,pady=10,columnspan=3)
if class_on_going!="it's not any class time":
    Label(root, text="Class Link:", font="Helvetica 25 bold", fg="red").grid(row=4, column=0, padx=10, pady=10)
    Button(root, text="open link!", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
           command=open_link).grid(row=4, column=1, padx=10, pady=10, columnspan=1)
    Button(root, text="Class details", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
           command=details_window).grid(row=4, column=2, padx=10, pady=10, columnspan=2)


Button(root, text="Add new class", font="helvetica 35 bold", fg="green", bg="black", borderless=1,
           command=add_class).grid(row=6, column=1, padx=10, pady=10, columnspan=3)
Button(root, text="Update Class", font="helvetica 35 bold", fg="green", bg="black", borderless=1,
          command=update_class).grid(row=7, column=1, padx=30, pady=10, columnspan=3)

Button(root, text="Delete Class", font="helvetica 35 bold", fg="green", bg="black", borderless=1,
           command=remove_class).grid(row=8, column=1, padx=30, pady=10, columnspan=3)





root.mainloop()