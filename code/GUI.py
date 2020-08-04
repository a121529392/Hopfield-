import tkinter as tk
from tkinter import ttk
from hop2 import *
import os
file=[]
noise=["10%","20%","30%","40%","50%","60%","70%","80%","90%"]
def get_file():
    files=os.listdir("./")
    for f in files:
        if "Testing.txt" in f:
            file.append(f)

def draw(data,N,P):
    hold=""
    for j in range(P):
        ch = ""
        for i in range(N):
            if data[j*N+i] == -1:
                ch += " "
            else:
                ch += "X"
            # ch += " " if data[j*N+i] == -1 else "X"
        hold+=ch
        hold+="\n"
    return hold
class Mainapplication():
    def __init__(self):
        self.pic=[]
        self.row = 0
        self.column = 0
        self.sample = []
        self.train=[]
        self.train_row = 0
        self.train_column = 0
        self.train_file=None
        self.weight=None

        tk.Label(root, text='Choose a file', font=('Consolas', 14)).place(x=20, y=10)
        self.combo_file = ttk.Combobox(root,values=file, font=('Consolas', 12))
        self.combo_file.bind('<<ComboboxSelected>>', self.get_pic)
        self.combo_file.place(x=20, y=40)
        self.combo_file.current(0)

        tk.Label(root, text='Choose a picture  ', font=('Consolas', 14)).place(x=270, y=10)
        self.combo_file2 = ttk.Combobox(root, values=None, font=('Consolas', 12))
        self.combo_file2.place(x=270, y=40)

        tk.Label(root, text='Add noise  ', font=('Consolas', 14)).place(x=540, y=10)
        self.combo_noise = ttk.Combobox(root, values=None, font=('Consolas', 12))
        self.combo_noise.place(x=540, y=40)


        tk.Label(root, text='Original Train Picture', font=('Consolas', 12)).place(x=20, y=270)
        tk.Label(root, text='Test Picture  ', font=('Consolas', 12)).place(x=300, y=120)
        tk.Label(root, text='Recover Test Picture  ', font=('Consolas', 12)).place(x=550, y=120)
        tk.Label(root, text='Add Noise Test Picture', font=('Consolas', 12)).place(x=250, y=450)
        tk.Label(root, text='Recover Noise Test Picture', font=('Consolas', 12)).place(x=520, y=450)

        self.ori_pic = tk.Label(root, textvariable="", font=("Consolas", 14))
        self.test_pic = tk.Label(root, textvariable="", font=("Consolas",14))
        self.re_test_pic = tk.Label(root, textvariable="", font=("Consolas", 14))
        self.nosie_test_pic = tk.Label(root, textvariable="", font=("Consolas", 14))
        self.re_nosie_test_pic = tk.Label(root, textvariable="", font=("Consolas", 14))

    def add_noise(self,event):
        pic = self.combo_file2.get()
        pic = pic.split("_")[1]
        value=self.combo_noise.get()
        print(value.split("%")[0])
        noise_train, noise_train_row, noise_train_column = read_sample(self.train_file)
        noise_pic=add_nosie(noise_train[int(pic)],value)

        ###noise_pic
        n_pic = draw(noise_pic, self.row, self.column)



        self.n_pic_var = tk.StringVar()
        self.n_pic_var.set(n_pic)
        self.nosie_test_pic.pack()
        self.nosie_test_pic.destroy()
        self.nosie_test_pic = tk.Label(root, textvariable=self.n_pic_var, font=("Consolas", 14))
        self.nosie_test_pic.place(x=250, y=480)

        ###re noise pic
        re_noise_pic = hop_run(noise_pic, self.weight)

        r_n_pic = draw(re_noise_pic, self.row, self.column)

        self.r_n_pic_var = tk.StringVar()
        self.r_n_pic_var.set(r_n_pic)
        self.re_nosie_test_pic.pack()
        self.re_nosie_test_pic.destroy()
        self.re_nosie_test_pic = tk.Label(root, textvariable=self.r_n_pic_var, font=("Consolas", 14))
        self.re_nosie_test_pic.place(x=520, y=480)



    def get_pic(self,event):
        f=self.combo_file.get()
        self.sample ,self.row,self.column= read_sample(f)
        if "Bonus" in f:
            self.train_file="./Bonus_Training.txt"
        else:
            self.train_file="./Basic_Training.txt"

        self.train, self.train_row, self.train_column=read_sample(self.train_file)
        self.caltrain, self.caltrain_row, self.caltrain_column = read_sample(self.train_file)
        self.weight = cal_weight(self.caltrain)
        hold=[]
        for i in range(0,len(self.sample),1):
            hold.append("pic_%s"%i)
        self.pic=hold

        self.combo_file2 = ttk.Combobox(root, values=self.pic, font=('Consolas', 12))
        self.combo_file2.bind('<<ComboboxSelected>>', self.draw_pic)
        self.combo_file2.place(x=270, y=40)
        self.combo_file2.current(0)

    def draw_pic(self,event):
        pic=self.combo_file2.get()
        pic=pic.split("_")[1]
        self.combo_noise = ttk.Combobox(root, values=noise, font=('Consolas', 12))
        self.combo_noise.bind('<<ComboboxSelected>>', self.add_noise)
        self.combo_noise.place(x=540, y=40)
        self.combo_noise.current(0)
        ###ori pic
        ori_pic = draw(self.train[int(pic)], self.row, self.column)
        print(ori_pic)

        self.ori_pic_var = tk.StringVar()
        self.ori_pic_var.set(ori_pic)
        self.ori_pic.pack()
        self.ori_pic.destroy()
        self.ori_pic = tk.Label(root, textvariable=self.ori_pic_var, font=("Consolas", 14))
        self.ori_pic.place(x=20, y=300)

        ###test pic
        test_pic=draw(self.sample[int(pic)],self.row,self.column)
        print(test_pic)

        self.pic_var = tk.StringVar()
        self.pic_var.set(test_pic)
        self.test_pic.pack()
        self.test_pic.destroy()
        self.test_pic = tk.Label(root, textvariable=self.pic_var, font=("Consolas",14))
        self.test_pic.place(x=300, y=150)

        ###test result pic
        test_res = hop_run(self.sample[int(pic)], self.weight)
        test_res_pic = draw(test_res, self.row, self.column)
        print(test_res_pic)

        self.test_res_pic_var = tk.StringVar()
        self.test_res_pic_var.set(test_res_pic)
        self.re_test_pic.pack()
        self.re_test_pic.destroy()
        self.re_test_pic = tk.Label(root, textvariable=self.test_res_pic_var, font=("Consolas", 14))
        self.re_test_pic.place(x=550, y=150)




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x800")
    get_file()
    print(file)

    application = Mainapplication()
    root.mainloop()