import xlrd
import numpy as np
from matplotlib import pyplot as plt
mp = {
        'data1.xlsx':'衬管（含水）',
        'data2.xlsx':'衬管（空气）'
}

class Solution:
    def calc(self,file,aim,f):

        Ts = 1.0/f

        workbook = xlrd.open_workbook(filename=r"./new/"+file)
        names = workbook.sheet_names()
        print("names: ", names)


        table = workbook.sheet_by_name(sheet_name=mp[file])
        row = table.nrows
        col = table.ncols
        print("row: ", row, "col: ", col)

        row_list = table.row_values(rowx=0, start_colx=0, end_colx=None)
        # print(row_list)

        col_list1 = table.col_values(colx=0, start_rowx=1, end_rowx=None)
        # print(col_list1)

        col_list2 = table.col_values(colx=aim, start_rowx=1, end_rowx=None)
        # print(col_list2)

        ti=[]
        for i in range(len(col_list1)):
            col_list1[i] = float(col_list1[i])
            col_list2[i] = float(col_list2[i])
            ti.append(Ts*i)

        print('type1: ',type(col_list1[0]))
        print('type2: ',type(col_list2))

        x = np.array(col_list1,dtype= np.float32)
        y = np.array(col_list2,dtype= np.float32)
        ti = np.array(ti, dtype= np.float32)

        plt.title('base')
        plt.stem(x,y)
        
        plt.savefig("./new/base.png")

        
        r1 = np.fft.fft(y)/y.size*2
        freq = np.fft.fftfreq(y.size)
        
        mag = abs(r1) # |r1|

        plt.figure(figsize=(40, 40))
        plt.subplot(221)
        plt.title('origin')
        plt.ylim((0,120))
        plt.stem(ti,y)
        plt.xlabel('Time /s')

        plt.subplot(222)
        plt.title('modulus')
        plt.ylim((0,130))
        plt.stem(col_list1,mag)
        plt.xlabel('Frequency /Hz')

        plt.subplot(223)
        plt.title('real')
        plt.ylim((-130,130))
        plt.xlabel('Frequency /Hz')
        plt.stem(col_list1,r1.real)

        plt.subplot(224)
        plt.title('imag')
        plt.ylim((-130,130))
        plt.xlabel('Frequency /Hz')
        plt.stem(col_list1,r1.imag)
        # plt.figure(figsize=(50,50))
        if file[-1]=='x':
            plt.savefig("./new/image_"+file[:-5]+".png")
        else:
            plt.savefig("./new/image_"+file[:-4]+".png")

if __name__=='__main__':
    file = "data2.xlsx"
    aim = 2
    f = 5
    Solution().calc(file=file,aim=aim,f=f)