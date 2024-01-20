import os
from tkinter import *
from driver import *
import pandas as pd
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

# Tạo một cửa sổ
class Doulingo_App ():

	def __init__(self,root):
		self.filename = None
		self.loaction = None
		self.link = None

		root.title("Lỗi ngữ pháp")
		root.geometry("800x530")

		label = Label( text="MÔN: KHOA HỌC DỮ LIỆU".upper(), font = ("Times New Roman", 24))
		label.place(x = 200, y = 10)

		label = Label( text="Giáo viên hướng dẫn: T.s Huỳnh Quang Đức", font = ("Times New Roman", 16))
		label.place(x = 210, y = 50)

		label = Label( text="Người thực hiện: Luyện Xuân Minh Đức", font = ("Times New Roman", 16))
		label.place(x = 230, y = 80)

		label = Label( text="Tệp tin chứa lỗi ngữ pháp: ")
		label.place(x = 50, y = 130)

		self.entry_filename = Entry(width = 44,font = ("Times New Roman",14))
		self.entry_filename.place(x = 195, y = 130)
# _____________________________________________________________________________________________

		button = Button( text="Chọn tệp tin", command=self.Open_File)
		button.place(x = 610, y = 129)

		self.text = Text(height=13, width = 61)
		self.text.place(x = 195, y = 175)
# _____________________________________________________________________________________________

		label = Label( text="Số lượng câu cần tạo: ")
		label.place(x = 50, y = 400)

		self.Number_of_Exercise = Entry(width = 44, font = ("Times New Roman",14))
		self.Number_of_Exercise.place(x = 195, y = 399)
		self.Number_of_Exercise.bind("<KeyRelease>", lambda event: self.validate_input())
# _____________________________________________________________________________________________

		label = Label( text="Chọn chỗ lưu bài tập: ")
		label.place(x = 50, y = 440)

		self.entry_location = Entry(width = 44, font = ("Times New Roman",14))
		self.entry_location.place(x = 195, y = 440)

		button = Button( text="  Tìm chỗ lưu  ", command=self.Saving_File)
		button.place(x = 610, y = 439)
# _____________________________________________________________________________________________

		button = Button( text="  Tạo bài  ", command=self.Run_Both)
		button.place(x = 330, y = 499)

		button = Button( text="  Thoát  ", command=root.quit)
		button.place(x = 450, y = 499)
# _____________________________________________________________________________________________

	def is_number(self,value):
	    try:
	        float(value)
	        return True
	    except ValueError:
	        return False

	def validate_input(self):
	    value = self.Number_of_Exercise.get()
	    if not self.is_number(value):
	        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số.")
	        self.Number_of_Exercise.delete(0,END)  # Xoá giá trị không phải số

# _____________________________________________________________________________________________

	def Note(self):
		note_label = Label( text="Note! 'Nhấn nút ”Tạo bài” để có một bài tập mới!' ")
		note_label.place(x = 530, y = 499)
# _____________________________________________________________________________________________

	def Open_File(self):
	    self.filename = askopenfilename()
	    self.entry_filename.insert(0, self.filename)

	    current_directory = os.path.dirname(os.path.abspath(__file__))
	    # Đọc file CSV vào DataFrame

	    with open(self.filename, "r", encoding="utf-8") as file:
	        raw_text = file.read()

	    self.text.delete(1.0, END)
	    self.text.insert(INSERT, raw_text)

	    # Chỉnh kích thước chữ xuống 10 pixel
	    

	    df = pd.read_csv(self.filename)

	    # Xóa các cột Loại lỗi, Miêu tả lỗi, Cách sửa lỗi
	    df.drop(['Loại lỗi', 'Miêu tả lỗi', 'Cách sửa lỗi'], axis=1, inplace=True)

	    output_directory = os.path.join(current_directory, 'output_folder')

	    # Tạo thư mục nếu nó chưa tồn tại
	    os.makedirs(output_directory, exist_ok=True)

	    # Đường dẫn đến tệp mới
	    output_file_path = os.path.join(output_directory, 'data.txt')

	    # Lưu DataFrame mới vào file CSV
	    df.to_csv(output_file_path, index=False)

	    self.link = output_file_path

	    return self.link

	def Saving_File(self):
	    self.location = askdirectory()
	    self.entry_location.insert(0, self.location)
	    return self.location
# _____________________________________________________________________________________________

	def Running_Action(self):
		Number_of_Exercise = float(self.Number_of_Exercise.get())
		Handle_text(self.link,Number_of_Exercise,self.location)
		messagebox.showinfo("Đã tạo thành công!!!")
# _____________________________________________________________________________________________

	def Run_Both(self):
		self.Running_Action()
		self.Note()

		


root = Tk()
Doulingo_App = Doulingo_App(root)
root.mainloop()
