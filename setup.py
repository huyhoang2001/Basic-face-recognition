import tkinter  # thư viện tạo giao diện
from tkinter import *  # lấy tất cả thư viện giao diện
from tkinter import messagebox as mess  # thư viện giao diện tin nhắn
from tkinter import ttk
import tkinter.simpledialog as tsd
import os  # thư viện cho phép truy cặp hệ thống
import cv2  # thư viện opencv
import csv  # thư viện opencv
# (Numerical Python) sử dụng để tính toán khoa học và làm việc với các mảng.
import numpy as np
# bao gồm các chức năng tải hình ảnh từ tệp và tạo hình ảnh mới.
from PIL import Image
# thư việ cung cấp dữ liệu và các phép toán để thao tác với các bảng số và chuỗi thời gian.
import pandas as pd
import datetime  # thư viện ngày giờ
import time  # thư viện thời gian
# Chức năng
# hàm thoát


def on_closing():
    if mess.askyesno("Thoát", "Bạn đang thoát khỏi cửa sổ. Bạn có muốn thoát không?"):
        window.destroy()
# nút xóa text


def clear():
    txt.delete(0, 'end')
    txt2.delete(0, 'end')
# kiểm tra đường dẫn


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
# kiểm tra tệp haarcascade


def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='đóng tập tin bị thiếu',
                   message='một số tệp bị thiếu. Vui lòng liên hệ với tôi để được trợ giúp')
        window.destroy()
# kiểm tra mặt khẩu và đổi mật khẩu


def save_pass():
    assure_path_exists("Pass_Train/")
    exists1 = os.path.isfile("Pass_Train\pass.txt")
    if exists1:
        tf = open("Pass_Train\pass.txt", "r")
        str = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring(
            'mật khẩu chưa được đặt', 'Vui lòng nhập mật khẩu mới bên dưới', show='*')
        if new_pas == None:
            mess._show(title='Mật khẩu rỗng đã nhập',
                       message='Mật khẩu chưa được đặt. Vui lòng thử lại!')
        else:
            tf = open("Pass_Train\pass.txt", "w")
            tf.write(new_pas)
            mess._show(title='Đã đăng ký mật khẩu!',
                       message='Mật khẩu mới đã được đăng ký thành công!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == str):
        if(newp == nnewp):
            txf = open("Pass_Train\pass.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Lỗi', message='Xác nhận lại mật khẩu mới !!!')
            return
    else:
        mess._show(title='Sai mật khẩu',
                   message='Vui lòng nhập đúng mật khẩu cũ.')
        return
    mess._show(title='Mật khẩu đã được thay đổi',
               message='Đã thay đổi mật khẩu thành công.')
    master.destroy()
# giao diện đổi mật khẩu


def change_pass():
    global master
    master = tkinter.Tk()
    master.iconbitmap("laptop.ico")
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Thay đổi mật khẩu quản trị viên")
    master.configure(background="white")
    lbl4 = tkinter.Label(master, text='         Mật khẩu hiện tại',
                         bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tkinter.Entry(master, width=25, fg="black",
                        relief='solid', font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tkinter.Label(master, text='               Mật khẩu mới',
                         bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tkinter.Entry(master, width=25, fg="black",
                        relief='solid', font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tkinter.Label(master, text=' Nhập lại mật khẩu mới',
                         bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tkinter.Entry(master, width=25, fg="black",
                         relief='solid', font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tkinter.Button(master, text="Hủy", command=master.destroy, fg="white",
                            bg="#13059c", height=1, width=25, activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tkinter.Button(master, text="Lưu", command=save_pass, fg="black", bg="#00aeff",
                           height=1, width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()
# câu hỏi mật khẩu


def psw():
    assure_path_exists("Pass_Train/")
    exists1 = os.path.isfile("Pass_Train\pass.txt")
    if exists1:
        tf = open("Pass_Train\pass.txt", "r")
        str_pass = tf.read()
    else:
        new_pas = tsd.askstring('Mật khẩu cũ không tìm thấy',
                                'Vui lòng nhập mật khẩu mới bên dưới', show='*')
        if new_pas == None:
            mess._show(title='Không có mật khẩu nào được nhập',
                       message='Mật khẩu chưa được đặt !! Vui lòng thử lại')
        else:
            tf = open("Pass_Train\pass.txt", "w")
            tf.write(new_pas)
            mess._show(title='Mật khẩu đã đăng ký',
                       message='Mật khẩu mới đã được đăng ký thành công !!')
            return
    password = tsd.askstring('Mật khẩu', 'Nhập mật khẩu', show='*')
    if (password == str_pass):
        TrainImages()

    elif (password == None):
        pass
    else:
        mess._show(title='Sai mật khẩu',
                   message='Bạn đã nhập sai mật khẩu')
# chụp ảnh


def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # sô lần tăng của sapleNum
                sampleNum = sampleNum + 1
                # lưu khuôn mặt dẫ chụp vào thư mục TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # hiển thị khung hình
                cv2.imshow('Taking Images', img)
            # đợi trong 100 mili giây
            if cv2.waitKey(100) & 0xFF == ord('x'):
                break
            # dừng nếu số lượng ảnh nhiều hơn 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Nhập tên chính xác"
            message.configure(text=res)
# xử lí ảnh


def TrainImages():
    check_haarcascadefile()
    assure_path_exists("Pass_Train/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='Không có đăng ký',
                   message='Please Register someone first!!!')
        return
    recognizer.save("Pass_Train\Trainner.yml")
    res = "Hồ sơ đã Lưu thành công"
    message1.configure(text=res)
    message.configure(text='Tổng số đăng ký cho đến nay  : ' + str(ID[0]))
# lấy Hình ảnh và Nhãn


def getImagesAndLabels(path):
    # lấy đường dẫn của tất cả các tệp trong thư mục
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # tạo danh sách khuôn mặt trống
    faces = []
    # tạo danh sách ID trống
    Ids = []
    # bây giờ lặp qua tất cả các đường dẫn hình ảnh và tải các id và hình ảnh
    for imagePath in imagePaths:
        # tải hình ảnh và chuyển đổi nó sang thang độ xám
        pilImage = Image.open(imagePath).convert('L')
        # Bây giờ chúng tôi đang chuyển đổi hình ảnh PIL thành mảng numpy
        imageNp = np.array(pilImage, 'uint8')
        # lấy Id từ hình ảnh
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # trích xuất khuôn mặt từ mẫu hình ảnh đào tạo
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids
# Theo dõi hình ảnh


def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tb.get_children():
        tb.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    exists3 = os.path.isfile("Pass_Train\Trainner.yml")
    if exists3:
        recognizer.read("Pass_Train\Trainner.yml")
    else:
        mess._show(title='Thiếu dữ liệu',
                   message='Vui lòng nhấp vào Lưu hồ sơ để thiết lập lại dữ liệu !!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Thiếu chi tiết',
                   message='Thông tin chi tiết về sinh viên còn thiếu, vui lòng kiểm tra!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 255), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(
                    ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date),
                              '', str(timeStamp)]
                cv2.putText(im, "Name: " + str(bb), (x, y + h + 30),
                            font, 1, (0, 255, 0), 2)
                cv2.putText(im, "ID: " + str(ID), (x, y + h + 60),
                            font, 1, (0, 255, 0), 2)
            else:
                Id = 'Unknown'
                bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h + 30),
                            font, 1, (0, 0, 255), 2)
        cv2.imshow('ĐIỂM DANH', im)
        if (cv2.waitKey(1) == ord('x')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tb.insert('', 0, text=iidd, values=(
                        str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()


# tạo giao diện
window = tkinter.Tk()
window.iconbitmap("laptop.ico")
window.title("Hệ thóng điểm danh")
window.geometry("1280x720")
window.resizable(True, True)
window.configure(background='#355454')

# Thanh menu trợ giúp
menubar = Menu(window)
help = Menu(menubar, tearoff=0)
help.add_command(label="Thay mật khẩu", command=change_pass)
help.add_separator()
help.add_command(label="Thoát", command=on_closing)
menubar.add_cascade(label="Trợ giúp", menu=help)

# Dòng này sẽ đính kèm menu của chúng ta vào cửa sổ
window.config(menu=menubar)

# cửa sổ chính
message3 = tkinter.Label(window, text="Hệ thống điểm danh khuông mặt",
                         fg="white", bg="#355454", width=60, height=1, font=('times', 29, ' bold '))
message3.place(x=10, y=10, relwidth=1)

# khung
frame1 = tkinter.Frame(window, bg="white")
frame1.place(relx=0.11, rely=0.15, relwidth=0.39, relheight=0.80)

frame2 = tkinter.Frame(window, bg="white")
frame2.place(relx=0.51, rely=0.15, relwidth=0.39, relheight=0.80)

# tiêu đề khung
fr_head1 = tkinter.Label(frame1, text="Đăng ký sinh viên mới",
                         fg="white", bg="black", font=('times', 17, ' bold '))
fr_head1.place(x=0, y=0, relwidth=1)

fr_head2 = tkinter.Label(frame2, text="Điểm danh học sinh",
                         fg="white", bg="black", font=('times', 17, ' bold '))
fr_head2.place(x=0, y=0, relwidth=1)

# khung đăng ký
lbl = tkinter.Label(frame1, text="Nhập ID:", width=15, height=1,
                    fg="black", bg="white", font=('times', 17, ' bold '))
lbl.place(x=0, y=55)

txt = tkinter.Entry(frame1, width=32, fg="black", bg="#e1f2f2",
                    highlightcolor="#00aeff", highlightthickness=3, font=('times', 15, ' bold '))
txt.place(x=55, y=88, relwidth=0.75)

lbl2 = tkinter.Label(frame1, text="Nhập tên:", width=15, height=1,
                     fg="black", bg="white", font=('times', 17, ' bold '))
lbl2.place(x=0, y=140)

txt2 = tkinter.Entry(frame1, width=32, fg="black", bg="#e1f2f2",
                     highlightcolor="#00aeff", highlightthickness=3, font=('times', 15, ' bold '))
txt2.place(x=55, y=173, relwidth=0.75)


message1 = tkinter.Label(frame1, text="", bg="white",
                         fg="black", width=39, height=1, activebackground="yellow", font=('times', 15, ' bold '))
message1.place(x=7, y=300)

message = tkinter.Label(frame1, text="", bg="white", fg="black", width=39,
                        height=1, activebackground="yellow", font=('times', 16, ' bold '))
message.place(x=7, y=500)
# Khung điểm danh
lbl3 = tkinter.Label(frame2, text="Bảng điểm danh", width=20,
                     fg="black", bg="white", height=1, font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

# hiển thị sô lượng thành viên----------
res = 0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Tổng số đăng ký : '+str(res))

# nút bấm----------------------------------------------

clearButton = tkinter.Button(frame1, text="xóa bộ nhớ cache", command=clear, fg="red",
                             bg="white", width=11, activebackground="blue", font=('times', 12, ' bold '))
clearButton.place(x=55, y=230, relwidth=0.29)

takeImg = tkinter.Button(frame1, text="Chụp ảnh", command=TakeImages, fg="black",
                         bg="#00aeff", width=34, height=1, activebackground="white", font=('times', 16, ' bold '))
takeImg.place(x=30, y=350, relwidth=0.89)

trainImg = tkinter.Button(frame1, text="Lưu thông tin", command=psw, fg="black", bg="#00aeff",
                          width=34, height=1, activebackground="white", font=('times', 16, ' bold '))
trainImg.place(x=30, y=430, relwidth=0.89)

trackImg = tkinter.Button(frame2, text="Điểm danh", command=TrackImages, fg="black",
                          bg="#00aeff", height=1, activebackground="white", font=('times', 16, ' bold '))
trackImg.place(x=30, y=60, relwidth=0.89)

quitWindow = tkinter.Button(frame2, text="Thoát", command=window.destroy, fg="white",
                            bg="#13059c", width=35, height=1, activebackground="white", font=('times', 16, ' bold '))
quitWindow.place(x=30, y=450, relwidth=0.89)


# bảng điểm danh----------------------------
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                font=('Calibri', 11))  # Sửa đổi phông chữ của phần nội dung
style.configure("mystyle.Treeview.Heading", font=(
    'times', 13, 'bold'))  # Sửa đổi phông chữ của tiêu đề
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
             'sticky': 'nswe'})])  # Xóa các đường viền
tb = ttk.Treeview(frame2, height=13, columns=(
    'name', 'date', 'time'), style="mystyle.Treeview")
tb.column('#0', width=82)
tb.column('name', width=130)
tb.column('date', width=133)
tb.column('time', width=133)
tb.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
tb.heading('#0', text='ID')
tb.heading('name', text='Tên')
tb.heading('date', text='Ngày')
tb.heading('time', text='Giờ')

# thanh cuộn--------------------------------------------------

scroll = ttk.Scrollbar(frame2, orient='vertical', command=tb.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tb.configure(yscrollcommand=scroll.set)

# thoát vòng lập------------------------------------------------
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
