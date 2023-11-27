from tkinter import *
import customtkinter
from PIL import ImageTk, Image

root = Tk()
root.title("CampusSystemV1")
root.geometry('1300x700')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

map_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
map_frame.place(x=100, y=60)

courses2_frame = Frame(root, width=screen_width, height=screen_height, bg='white')
courses2_frame.place(x=100, y=60)

courses3_frame = Frame(root, width=screen_width, height=screen_height, bg='white')
courses3_frame.place(x=100, y=60)

courses_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
courses_frame.place(x=100, y=60)

coursesbg = Frame(courses_frame, width='940', height='500', bg='#2C384A')
coursesbg.place(x=150, y=45)

coursesbg2 = Frame(courses2_frame, width='940', height='500', bg='#2C384A')
coursesbg2.place(x=150, y=45)

coursesbg3 = Frame(courses3_frame, width='940', height='500', bg='#2C384A')
coursesbg3.place(x=150, y=45)

teachers_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
teachers_frame.place(x=100, y=60)

contactus_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
contactus_frame.place(x=100, y=60)

header1 = Frame(root, width=screen_width, height='10', bg='sky blue')
header1.place(x=0, y=0)

header = Frame(root, width=screen_width, height='50', bg='#4472C4')
header.place(x=0, y=10)

home = Label(header, text="Welcome to STI Campus System", fg="white", font="Arial 22", bg='#4472C4')
home.place(x=100, y=10)

logo1 = (Image.open("STI LOGO.png"))
resized_image = logo1.resize((80, 48), Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized_image)

nemu = Frame(root, width='100', height=screen_height, bg='#2C384A')
nemu.place(x=0, y=60)

coursesbg = Frame(courses_frame, width='940', height='500', bg='#2C384A')
coursesbg.place(x=150, y=100)

home = Label(map_frame, text="STI Building Map", fg="Black", font="Arial 22", bg='white')
home.place(x=480, y=50)

articles_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
articles_frame.place(x=100, y=60)

img_articles = (Image.open("Articles.png"))
resized_image2 = img_articles.resize((1033, 486), Image.LANCZOS)
new_articles = ImageTk.PhotoImage(resized_image2)

articles_img_lbl = Label(articles_frame, image=new_articles, activebackground='white', bg='white')
articles_img_lbl.place(x=100, y=100)

news_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
news_frame.place(x=100, y=60)

img_news = (Image.open("News.png"))
resized_image3 = img_news.resize((1033, 486), Image.LANCZOS)
new_news = ImageTk.PhotoImage(resized_image3)

news_img_lbl = Label(news_frame, image=new_news, activebackground='white', bg='white')
news_img_lbl.place(x=100, y=100)

enroll_frame = Frame(root, width=screen_width, height=screen_height, bg='White')
enroll_frame.place(x=100, y=60)

img_enroll = (Image.open("EnrollOnline.png"))
resized_image1 = img_enroll.resize((1043, 496), Image.LANCZOS)
new_enroll = ImageTk.PhotoImage(resized_image1)

enroll_img_lbl = Label(enroll_frame, image=new_enroll, activebackground='white', bg='white')
enroll_img_lbl.place(x=95, y=100)

stiprogs = Label(courses_frame, text="STI Programs", fg="yellow", font="Arial 15", bg='#2C384A')
stiprogs.place(x=200, y=105)

sliderbutton = (Image.open("SliderButton.png"))
resized_image4 = sliderbutton.resize((68, 20), Image.LANCZOS)
new_sliderbutton = ImageTk.PhotoImage(resized_image4)


enroll_button = Button(enroll_frame, image=new_sliderbutton, command=enroll_frame.lift, borderwidth=0,
                       activeforeground='white', activebackground='white')
articles_button = Button(enroll_frame, image=new_sliderbutton, command=articles_frame.lift, borderwidth=0,
                         activeforeground='white', activebackground='white')
news_button = Button(enroll_frame, image=new_sliderbutton, command=news_frame.lift, borderwidth=0,
                     activeforeground='white', activebackground='white')
sti_button = Button(nemu, image=new_logo, command=enroll_frame.lift, borderwidth=0,
                    bg='#2C384A', activebackground='#2C384A')

enroll_button1 = Button(news_frame, image=new_sliderbutton, command=enroll_frame.lift, borderwidth=0,
                        activeforeground='white', activebackground='white')
articles_button1 = Button(news_frame, image=new_sliderbutton, command=articles_frame.lift, borderwidth=0,
                          activeforeground='white', activebackground='white')
news_button1 = Button(news_frame, image=new_sliderbutton, command=news_frame.lift, borderwidth=0,
                      activeforeground='white', activebackground='white')

enroll_button2 = Button(articles_frame, image=new_sliderbutton, command=enroll_frame.lift, borderwidth=0,
                        activeforeground='white', activebackground='white')
articles_button2 = Button(articles_frame, image=new_sliderbutton, command=articles_frame.lift, borderwidth=0,
                          activeforeground='white', activebackground='white')
news_button2 = Button(articles_frame, image=new_sliderbutton, command=news_frame.lift, borderwidth=0,
                      activeforeground='white', activebackground='white')

enroll_button.place(x=460, y=60)
articles_button.place(x=560, y=60)
news_button.place(x=660, y=60)

enroll_button1.place(x=460, y=60)
articles_button1.place(x=560, y=60)
news_button1.place(x=660, y=60)

enroll_button2.place(x=460, y=60)
articles_button2.place(x=560, y=60)
news_button2.place(x=660, y=60)
sti_button.place(x=9, y=10)

collegecourses = (Image.open("CollegeCourses.png"))
resized_image13 = collegecourses.resize((800, 400), Image.LANCZOS)
new_collegecourses = ImageTk.PhotoImage(resized_image13)

shscourses = (Image.open("SHSCourses.png"))
resized_image14 = shscourses.resize((800, 400), Image.LANCZOS)
new_shscourses = ImageTk.PhotoImage(resized_image14)

coursescollege = (Image.open("CoursesCollege.png"))
resized_image11 = coursescollege.resize((400, 400), Image.LANCZOS)
new_coursescollege = ImageTk.PhotoImage(resized_image11)

coursesshs = (Image.open("CoursesSHS.png"))
resized_image12 = coursesshs.resize((400, 400), Image.LANCZOS)
new_coursesshs = ImageTk.PhotoImage(resized_image12)

homeicon = (Image.open("Home Icon.png"))
resized_image5 = homeicon.resize((40, 40), Image.LANCZOS)
new_homeicon = ImageTk.PhotoImage(resized_image5)

mapicon = (Image.open("Map icon.png"))
resized_image6 = mapicon.resize((40, 40), Image.LANCZOS)
new_mapicon = ImageTk.PhotoImage(resized_image6)

coursesicon = (Image.open("Courses.png"))
resized_image7 = coursesicon.resize((40, 40), Image.LANCZOS)
new_coursesicon = ImageTk.PhotoImage(resized_image7)

teachersicon = (Image.open("Teacher Icon.png"))
resized_image8 = teachersicon.resize((40, 40), Image.LANCZOS)
new_teachersicon = ImageTk.PhotoImage(resized_image8)

contactusicon = (Image.open("ContactUs Icon.png"))
resized_image9 = contactusicon.resize((40, 40), Image.LANCZOS)
new_contactusicon = ImageTk.PhotoImage(resized_image9)

map_buildmap = (Image.open("BuildingMap.png"))
resized_image10 = map_buildmap.resize((1043, 496), Image.LANCZOS)
new_buildmap = ImageTk.PhotoImage(resized_image10)

map_img_lbl = Label(map_frame, image=new_buildmap, activebackground='white', bg='white')
map_img_lbl.place(x=95, y=100)

home_button = customtkinter.CTkButton(master=nemu, image=new_homeicon, text="Home", width=90,
                                      height=40, compound="top", hover_color="#8296B0", fg_color='#2C384A',
                                      corner_radius=0, command=enroll_frame.lift)

home_button.place(x=5, y=80)

map_button = customtkinter.CTkButton(master=nemu, image=new_mapicon, text="Map", width=90,
                                     height=40, compound="top", hover_color="#8296B0", fg_color='#2C384A',
                                     corner_radius=0, command=map_frame.lift)
map_button.place(x=5, y=160)

courses_button = customtkinter.CTkButton(master=nemu, image=new_coursesicon, text="Courses",
                                         width=90, height=40, compound="top", hover_color="#8296B0",
                                         fg_color='#2C384A', corner_radius=0, command=courses_frame.lift)
courses_button.place(x=5, y=240)

teachers_button = customtkinter.CTkButton(master=nemu, image=new_teachersicon, text="teachers",
                                          width=90, height=40, compound="top", hover_color="#8296B0",
                                          fg_color='#2C384A', corner_radius=0, command=teachers_frame.lift)
teachers_button.place(x=5, y=320)

contactus_button = customtkinter.CTkButton(master=nemu, image=new_contactusicon, text="Contact Us",
                                           width=90, height=40, compound="top", hover_color="#8296B0",
                                           fg_color='#2C384A', corner_radius=0, command=contactus_frame.lift)
contactus_button.place(x=5, y=400)

ba_button = customtkinter.CTkButton(master=map_img_lbl, text="Building A", width=180, height=50, compound="top",
                                    hover_color='#2C384A', fg_color='black')
ba_button.place(x=40, y=130)

bb_button = customtkinter.CTkButton(master=map_img_lbl, text="Building B(N/A)", width=180, height=50, compound="top",
                                    hover_color='#2C384A', fg_color='grey', hover=False)
bb_button.place(x=40, y=190)

bc_button = customtkinter.CTkButton(master=map_img_lbl, text="Building C", width=180, height=50, compound="top",
                                    hover_color='#2C384A', fg_color='black')
bc_button.place(x=40, y=250)

bd_button = customtkinter.CTkButton(master=map_img_lbl, text="Building D", width=180, height=50, compound="top",
                                    hover_color='#2C384A', fg_color='black')
bd_button.place(x=40, y=310)

collcor_img_lbl = Label(courses2_frame, image=new_collegecourses, activebackground='white', bg='white')
collcor_img_lbl.place(x=220, y=90)

shscor_img_lbl = Label(courses3_frame, image=new_shscourses, activebackground='white', bg='white')
shscor_img_lbl.place(x=220, y=90)

college_button = Button(courses_frame, image=new_coursescollege, borderwidth=0, bg='white', activebackground='white',
                        command=courses2_frame.lift)
shs_button = Button(courses_frame, image=new_coursesshs, borderwidth=0, bg='white', activebackground='white',
                    command=courses3_frame.lift)

courses_backbutton = customtkinter.CTkButton(master=courses2_frame, text="Back",
                                             width=90, height=40, hover_color="#8296B0",
                                             fg_color='grey', command=courses_frame.lift)
courses_backbutton.place(x=20, y=50)

courses_backbutton2 = customtkinter.CTkButton(master=courses3_frame, text="Back",
                                              width=90, height=40, hover_color="#8296B0",
                                              fg_color='grey', command=courses_frame.lift)
courses_backbutton2.place(x=20, y=50)

college_button.place(x=200, y=155)
shs_button.place(x=640, y=155)

start_frame = Frame(root, width=screen_width, height=screen_height, bg='sky blue')
start_frame.pack(fill=BOTH, expand=True)

img_start = (Image.open("StartIcon.png"))
resized_image20 = img_start.resize((10, 10), Image.LANCZOS)
new_starticon = ImageTk.PhotoImage(resized_image20)

start_button = customtkinter.CTkButton(master=start_frame, text="Start",
                                       width=200, height=50, fg_color='#D35C58', image=new_starticon,
                                       command=start_frame.forget, border_width=0, corner_radius=200)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

img_lntk = (Image.open("Lintech Logo.png"))
resized_image212 = img_lntk.resize((135, 55), Image.LANCZOS)
new_lntk = ImageTk.PhotoImage(resized_image212)

lntk_img_lbl = Label(header, image=new_lntk, bg='#4472C4')
lntk_img_lbl.place(x=1150, y=-5)

img_teacherslbl = (Image.open("teacherlbl.png"))
resized_image21 = img_teacherslbl.resize((1100, 550), Image.LANCZOS)
new_teacherslbl = ImageTk.PhotoImage(resized_image21)


teachers_img_lbl = Label(teachers_frame, text="Faculty Staff", image=new_teacherslbl, activebackground='white',
                         bg='white')
teachers_img_lbl.place(x=100, y=50)

img_contactus = (Image.open("ContactUs.png"))
resized_image25 = img_contactus.resize((1100, 550), Image.LANCZOS)
new_contactus = ImageTk.PhotoImage(resized_image25)

teachers_img_lbl = Label(contactus_frame, text="Faculty Staff", image=new_contactus,
                         activebackground='white', bg='white')
teachers_img_lbl.place(x=100, y=50)

#root.attributes('-fullscreen', True)

root.mainloop()