from tkinter import *
from tkmacosx import *
from mysql.connector import *
from time import *
import webbrowser as web
from tkinter import ttk

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
#Ftime_now=600

count=1

point= mydb.cursor()


point.execute("select * from routine where days Like %s",[today+'%'])
classes=point.fetchall()

cursor=mydb.cursor()
cursor.execute('Select * from routine')
print(cursor)
rows=cursor.fetchall()
total=cursor.rowcount
print('total: '+ str(total))


def remove_from_database(a):
  sql = "DELETE FROM routine WHERE NO = %s"
  adr = (a, )
  new=mydb.cursor()
  new.execute(sql,adr)
  mydb.commit()


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
print(time_slot)

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



def update_day(a,n):
  if len(a)!=0:
    sql="update routine set days=%s where NO = %s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_course(a,n):
  if len(a)!=0:
    sql="update routine set course_name=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_short(a,n):
  if len(a)!=0:
    sql="update routine set short_name=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_teacher(a,n):
  if len(a)!=0:
    sql="update routine set teacher_name=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_code(a,n):
  if len(a)!=0:
    sql="update routine set course_code=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_start(a,n):
  if len(a)!=0:
    sql="update routine set start_time=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_end(a,n):
  if len(a)!=0:
    sql="update routine set end_time=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()

def update_meet(a,n):
  if len(a)!=0:
    sql="update routine set meet_link=%s where NO=%s"
    val=(a,int(n),)
    cursor.execute(sql,val)
    mydb.commit()










root=Tk();
root.geometry('900x1000')
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



def all_classes():
  nroot = Toplevel(root)
  nroot.title('All Classes')
  nroot.geometry("1200x1000")
  nroot.configure(bg='#faf598')
  columns=('NO','Day','Course Name','Short Name','Teacher Name',"Course Code",'Start Time',"End Time",'Meet Link')


  temp=ttk.Treeview(nroot)
  temp['columns']=columns
  temp.column('#0',width=0)
  temp.column('NO',anchor=CENTER,width=30)
  temp.column('Day', anchor=CENTER, width=120)
  temp.column('Course Name', anchor=CENTER, width=120)
  temp.column('Short Name',anchor=CENTER,width=120)
  temp.column('Teacher Name', anchor=CENTER, width=120)
  temp.column('Course Code', anchor=CENTER, width=120)
  temp.column('Start Time', anchor=CENTER, width=120)
  temp.column('End Time', anchor=CENTER, width=120)
  temp.column('Meet Link', anchor=CENTER, width=300)




  temp.heading('#0',text='',anchor=W)
  temp.heading('NO', text='NO', anchor=CENTER)
  temp.heading('Day', text='Day', anchor=CENTER)
  temp.heading('Course Name', text='Course Name', anchor=CENTER)
  temp.heading('Short Name', text='Short Name', anchor=CENTER)
  temp.heading('Teacher Name', text="Teacher's Name", anchor=CENTER)
  temp.heading('Course Code', text='Course Code', anchor=CENTER)
  temp.heading('Start Time', text='Start Time', anchor=CENTER)
  temp.heading('End Time', text='End Time', anchor=CENTER)
  temp.heading('Meet Link', text='Meet Link', anchor=CENTER)

  for i in rows:
    global count
    temp.insert('','end',iid=count,values=i)
    count+=1

  temp.pack()
  frame = Frame(nroot)
  frame.pack()

  Label(frame, text='Day',font="Helvetica 15 bold",bg='light blue').grid(row=1,column=1,padx=10,pady=10)
  Label(frame, text='Course Name', font="Helvetica 15 bold",bg='light blue').grid(row=1, column=2,padx=10,pady=10)
  Label(frame, text='Short Name',font="Helvetica 15 bold",bg='light blue').grid(row=1,column=3,padx=10,pady=10)
  Label(frame, text='Teacher Name', font="Helvetica 15 bold",bg='light blue').grid(row=1, column=4,padx=10,pady=10)
  Label(frame, text='Course Code', font="Helvetica 15 bold", bg='light blue').grid(row=1, column=5, padx=10, pady=10)
  Label(frame, text='Start Time', font="Helvetica 15 bold", bg='light blue').grid(row=1, column=6, padx=10, pady=10)
  Label(frame, text='End Time', font="Helvetica 15 bold", bg='light blue').grid(row=1, column=7, padx=10, pady=10)
  Label(frame, text='Meet Link', font="Helvetica 15 bold", bg='light blue').grid(row=1, column=8, padx=10, pady=10)


  day_entry=Entry(frame,width=10)
  day_entry.grid(row=2,column=1,padx=10,pady=10)
  course_name_entry=Entry(frame,width=10)
  course_name_entry.grid(row=2,column=2,padx=10,pady=10)
  short_name_entry=Entry(frame,width=10)
  short_name_entry.grid(row=2,column=3,padx=10,pady=10)
  teacher_name_entry=Entry(frame,width=10)
  teacher_name_entry.grid(row=2,column=4,padx=10,pady=10)

  course_code_entry=Entry(frame,width=10)
  course_code_entry.grid(row=2,column=5,padx=10,pady=10)

  start_time_entry=Entry(frame,width=10)
  start_time_entry.grid(row=2,column=6,padx=10,pady=10)

  end_time_entry=Entry(frame,width=10)
  end_time_entry.grid(row=2,column=7,padx=10,pady=10)
  meet_link_entry=Entry(frame,width=10)
  meet_link_entry.grid(row=2, column=8, padx=10, pady=10)
  def add_data():
    global total
    total+=1
    day=day_entry.get()
    course=course_name_entry.get()
    short=short_name_entry.get()
    teacher=teacher_name_entry.get()
    code=course_code_entry.get()
    start_time=start_time_entry.get()
    end_time=end_time_entry.get()
    meet=meet_link_entry.get()

    if len(day)!=0 and len(course)!=0 and len(short)!=0 and len(teacher)!=0 and len(code)!=0 and len(start_time)!=0 and len(end_time)!=0 and len(meet)!=0:
      global count
      temp.insert('', 'end',iid=count, values=(count,day,course,short,teacher,code,start_time,end_time,meet))
      sql=("INSERT INTO routine (NO,days,course_name,short_name,teacher_name,course_code,start_time,end_time,meet_link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
      value=(count,day,course,short,teacher,code,start_time,end_time,meet)
      cursor.execute(sql,value)
      mydb.commit()
      print(cursor)
      count+=1

    day_entry.delete(0,END)
    course_name_entry.delete(0,END)
    short_name_entry.delete(0,END)
    teacher_name_entry.delete(0,END)
    course_code_entry.delete(0,END)
    start_time_entry.delete(0,END)
    end_time_entry.delete(0,END)
    meet_link_entry.delete(0,END)


  def remove_data():
    global count
    global cursor
    x=temp.selection()[0]
    print(x)
    temp.delete(x)
    remove_from_database(x)

    count-=1






  Button(frame, text="Add Data", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
         command=add_data).grid(row=3, column=2, padx=10, pady=10, columnspan=2)
  Button(frame, text="Remove Data", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
         command=remove_data).grid(row=3, column=5, padx=10, pady=10, columnspan=2)

  Label(frame, text='NO*', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=1, padx=10, pady=10)
  Label(frame, text='Day', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=2, padx=10, pady=10)
  Label(frame, text='Course Name', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=3, padx=10, pady=10)
  Label(frame, text='Short Name', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=4, padx=10, pady=10)
  Label(frame, text='Teacher Name', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=5, padx=10, pady=10)
  Label(frame, text='Course Code', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=6, padx=10, pady=10)
  Label(frame, text='Start Time', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=7, padx=10, pady=10)
  Label(frame, text='End Time', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=8, padx=10, pady=10)
  Label(frame, text='Meet Link', font="Helvetica 15 bold", bg='light blue').grid(row=4, column=9, padx=10, pady=10)


  no_data=Entry(frame, width=10)
  no_data.grid(row=5, column=1, padx=10, pady=10)
  day_data = Entry(frame, width=10)
  day_data.grid(row=5, column=2, padx=10, pady=10)
  course_name_data = Entry(frame, width=10)
  course_name_data.grid(row=5, column=3, padx=10, pady=10)
  short_name_data = Entry(frame, width=10)
  short_name_data.grid(row=5, column=4, padx=10, pady=10)
  teacher_name_data = Entry(frame, width=10)
  teacher_name_data.grid(row=5, column=5, padx=10, pady=10)

  course_code_data = Entry(frame, width=10)
  course_code_data.grid(row=5, column=6, padx=10, pady=10)

  start_time_data = Entry(frame, width=10)
  start_time_data.grid(row=5, column=7, padx=10, pady=10)

  end_time_data = Entry(frame, width=10)
  end_time_data.grid(row=5, column=8, padx=10, pady=10)
  meet_link_data = Entry(frame, width=10)
  meet_link_data.grid(row=5, column=9, padx=10, pady=10)



  def temp_update_data():
    number=no_data.get()
    if len(number)!=0:
      check_=True
      for i in number:
        if i<'0' or i>'9':

          check_=False
          break

    if check_:
     print(type(no_data.get()),no_data.get())
     update_course(course_name_data.get(), no_data.get())
     update_short(short_name_data.get(), no_data.get())
     update_teacher(teacher_name_data.get(), no_data.get())
     update_code(course_code_data.get(), no_data.get())
     update_start(start_time_data.get(), no_data.get())
     update_end(end_time_data.get(), no_data.get())
     update_meet(meet_link_data.get(), no_data.get())
     update_day(day_data.get(), no_data.get())
    else:
      print('invalid number!')


  Button(frame, text="Update data", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
         command=temp_update_data).grid(row=6, column=4, padx=20, pady=10, columnspan=2)









Label(root,bg='#faefcf').grid(row=0,column=0,columnspan=6)
Label(root,text="Time:",font="Helvetica 40 bold",fg="red").grid(row=1,column=0,padx=10,pady=10)
Label(root,text="8:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=1,padx=10,pady=10)
Label(root,text="10:00",font="Helvetica 40 bold",fg="red").grid(row=1,column=2,padx=10,pady=10)
Label(root,text="11:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=3,padx=10,pady=10)
Label(root,text="1:00",font="Helvetica 40 bold",fg="red").grid(row=1,column=4,padx=10,pady=10)
Label(root,text="2:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=5,padx=10,pady=10)
Label(root,text="Today's class:",font="Helvetica 25 bold",fg="red").grid(row=2,column=0,padx=10,pady=10)

if len(classes)==0:
  Label(root, text="there is no class today!", font="helvetica 25 bold", fg="red").grid(row=2, column=1, padx=10,pady=10, columnspan=3)
else :
  for i in time_slot:
    if i==510:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=1, padx=10, pady=10)
    if i == 600:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=2, padx=10, pady=10)
    elif i == 690:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=3, padx=10, pady=10)
    elif i == 780:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=4, padx=10, pady=10)
    elif i == 870:
      Label(root, text=time_slot[i], font="helvetica 25 bold", fg="red").grid(row=2, column=5, padx=10, pady=10)
Label(root,text="Class on going:",font="Helvetica 25 bold",fg="red").grid(row=3,column=0,padx=10,pady=10)
Label(root,text=class_on_going,font="Helvetica 25 bold",fg="red").grid(row=3,column=1,padx=10,pady=10,columnspan=3)
if class_on_going!="it's not any class time":
    Label(root, text="Class Link:", font="Helvetica 25 bold", fg="red").grid(row=4, column=0, padx=10, pady=10)
    Button(root, text="open link!", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
           command=open_link).grid(row=4, column=1, padx=10, pady=10, columnspan=1)
    Button(root, text="Class details", font="helvetica 25 bold", fg="green", bg="black", borderless=1,
           command=details_window).grid(row=4, column=2, padx=10, pady=10, columnspan=2)


Button(root, text="Show Database", font="helvetica 35 bold", fg="red", bg="black", borderless=1,
           command=all_classes).grid(row=5, column=1, padx=30, pady=10, columnspan=3)






root.mainloop()