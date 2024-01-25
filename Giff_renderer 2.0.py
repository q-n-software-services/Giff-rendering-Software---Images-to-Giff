import os
import random
from PIL import Image, ImageDraw
import glob
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout,QLineEdit, QPushButton, QHBoxLayout, QLCDNumber, QLabel, QWidget, QFileDialog
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from PIL import Image

a = chr(34)
image_link12 = None

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(272, 72, 800, 600)
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setWindowTitle("\t yoycolors")
        self.setWindowIcon(QIcon("burger.ico"))


        self.lcd_number()

    def lcd_number(self):

        vbox = QVBoxLayout()
        self.label = QLabel("      yoycolors")
        self.label.setStyleSheet("background-color:Yellow")
        self.label.setFont(QFont("times new roman", 48))
        self.label.setFixedHeight(120)
        vbox.addWidget(self.label)

        self.label2 = QLabel("      ONLY use OPEN button i.e. file explorer for images, don't use for selecting folders\n"
                             "      Software will automatically get the folder link from that image's link\n"
                             "      *** OR *** Copy the Folder Path and paste in respective box\n"
                             "      # Give a custom name to the GIFF file\n")
        self.label2.setStyleSheet("color:red")
        self.label2.setFont(QFont("times new roman", 12))
        self.label2.setFixedHeight(77)

        hbox = QHBoxLayout()

        self.label3 = QLabel(" NOTE  ")
        self.label3.setStyleSheet("color:Red")
        self.label3.setFont(QFont("castellar", 27))
        self.label3.setFixedHeight(72)
        self.label3.setFixedWidth(144)

        hbox.addWidget(self.label3)
        hbox.addWidget(self.label2)

        vbox.addLayout(hbox)



        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("\tEnter the Folder link here")
        self.input1.setFont(QFont("times new roman", 12))
        self.input1.setFixedHeight(60)
        self.input1.setStyleSheet("background-color:white")
        hbox12 = QHBoxLayout()
        hbox12.addWidget(self.input1)

        btn2 = QPushButton(" OPEN ")
        btn2.setFont(QFont("times new roman", 29))
        btn2.setStyleSheet("background-color:green")
        btn2.setFixedWidth(120)
        btn2.clicked.connect(self.open)
        hbox12.addWidget(btn2)

        vbox.addLayout(hbox12)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox3 = QHBoxLayout()

        self.label4 = QLabel(" NAME   ")
        self.label4.setStyleSheet("color:indigo")
        self.label4.setFont(QFont("castellar", 27))
        self.label4.setFixedHeight(72)
        self.label4.setFixedWidth(144)
        hbox3.addWidget(self.label4)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("\tEnter Name of the Giff that will be exported")
        self.input2.setFont(QFont("times new roman", 12))
        self.input2.setFixedHeight(60)
        self.input2.setStyleSheet("background-color:white")
        hbox3.addWidget(self.input2)

        vbox.addLayout(hbox3)

        '''btn1 = QPushButton(" Export .gif ")
        btn1.setFont(QFont("times new roman", 36))
        btn1.setStyleSheet("background-color:pink")
        btn1.clicked.connect(self.giff)
        hbox1.addWidget(btn1)'''

        btn3 = QPushButton("  Render Giff")
        btn3.setFont(QFont("times new roman", 36))
        btn3.setStyleSheet("background-color:pink")
        btn3.clicked.connect(self.all_images)
        hbox2.addWidget(btn3)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def open(self):
        global image_link12
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):

            image_link12 = path[0]

    def giff(self):
        b = chr(92)
        global image_link12
        image_link = self.input1.text().lstrip().rstrip()
        if image_link12 == None:
            if image_link == "":
                return
            else:
                stripper = image_link.split(a)

                image_link = stripper[1]

        else:
            image_link = image_link12

        print(image_link)

        my_image = Image.open(image_link)
        output_name = self.input2.text().lstrip().rstrip()
        out_list = list(image_link)

        c = out_list[2]

        out_list2 = image_link.split(c)
        d = len(out_list2) - 1
        temp = out_list2.pop(d)
        out_list3 = [(item.lstrip().rstrip() + c[0]) for item in out_list2]

        num = random.randint(0, 999)
        num = str(num)
        if output_name == "":
            output_name = "Untitled" + num

        out_name_prefix = ""
        out_name_prefix = out_name_prefix.join(out_list3)
        out_name_prefix = out_name_prefix.lstrip().rstrip()
        output_name_final = out_name_prefix + output_name

        # folder_path = out_name_prefix

        output_name_final += '.gif'
        my_image.save(output_name_final, 'gif')

    def all_images(self):
        image_list = []
        b = chr(92)
        c = chr(47)
        global image_link12
        image_link = self.input1.text().lstrip().rstrip()
        if image_link12 == None:
            if image_link == "":
                return
            else:
                stripper = image_link.split(a)

                image_link = stripper[1]

        else:
            image_link = image_link12
        print(image_link)
        if image_link[2] == b:
            temp = image_link.split(b)
            print(temp)
            temp2 = temp.pop(len(temp) - 1)
            folder_link = b.join(temp)
        elif image_link[2] == c:
            temp = image_link.split(c)
            print(temp)
            temp2 = temp.pop(len(temp) - 1)
            folder_link = c.join(temp)
        print(folder_link)

        path = folder_link
        if path == "":
            return
        print(path)
        output_name = self.input2.text().lstrip().rstrip()
        if output_name == "":
            num = random.randint(100, 999)
            num = str(num)
            output_name = "Untitled" + num

        '''num = random.randint(0, 999)
        num = str(num)
        path_new = path + '\\Giff_Images' + num
        os.mkdir(path_new)
            path2 = path + '/*.jpg'
        for filename in glob.glob(path2):  # assuming jpg
            im = Image.open(filename)
            temp_img = filename.split('.')
            temp2 = temp_img[0]
            path_broken = temp2.split(b)
            i = len(path_broken) - 1
            new_img = path_broken[i]
            new_img = b + new_img
            print(new_img)

            new_img = path_new + new_img + ".gif"

            image_list.append(filename)
            im.save(new_img, 'gif')'''

        path3 = path + '/*.png'
        frames = []
        # Create the frames
        imgs = glob.glob(path3)
        frames = []
        for i in imgs:
            new_frame = Image.open(i)
            frames.append(new_frame)

        # Save into a GIFF file that loops forever
        path4 = path + '/' + output_name + '.gif'
        frames[0].save(path4, format='GIF',
                       append_images=frames[1:],
                       save_all=True,
                       duration=300, loop=0)

        '''for filename in glob.glob(path3):  # assuming png
            im = Image.open(filename)
            temp_img = filename.split('.')
            temp2 = temp_img[0]
            path_broken = temp2.split(b)
            i = len(path_broken) - 1
            new_img = path_broken[i]
            new_img = b + new_img
            print(new_img)

            new_img = path_new + new_img + ".gif"

            image_list.append(im)
            im.save(new_img, 'gif')
        print(image_list)

        image_list[0].save('png_to_gif.gif', format='GIF', append_images=image_list[1:], save_all=True, duration=300, loop=0)'''



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

