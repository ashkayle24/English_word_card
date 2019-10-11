import random
from os import listdir
from os.path import isfile, isdir, join
import shutil
import os

Word_list = list()
file_nun = ['21','13','8','5','3','2','1']
mypath = 'D:\\Eng'
file_len = len(file_nun)
count = 0

while (count < file_len ):
    files = listdir(mypath + '\\' + file_nun[count])
    for f in files:
        fullpath = join(mypath,file_nun[count], f)
        if isfile(fullpath):
            print("檔案：", fullpath)

            f_list = open(fullpath, 'r', encoding='UTF-8')

            for Read_i in f_list:
                Read_i = Read_i.replace('\n', '')
                String_temp = Read_i.split(',')
                Word_list.append(String_temp[0])
                Word_list.append(String_temp[1])
                Word_list.append(String_temp[2])
            f_list.close()

            random_count = (len(Word_list)) / 3

            while (random_count > 0):
                Read_Nun = random.randint(1, random_count)
                Read_Nun = (Read_Nun * 3) - 3
                print(Word_list[Read_Nun + 1] + ',' + Word_list[Read_Nun + 2])

                print('type the word:')
                Check_Know = input()
                if Check_Know == Word_list[Read_Nun]:
                    del Word_list[Read_Nun + 2]
                    del Word_list[Read_Nun + 1]
                    del Word_list[Read_Nun]
                else:
                    print(Word_list[Read_Nun])
                # print(len(Word_list))
                random_count = (len(Word_list)) / 3

            if (file_nun[count]) == '21':
                shutil.copyfile(fullpath , mypath + '\\final\\' + f)
                os.remove(fullpath)
            else:
                shutil.copyfile(fullpath, mypath + '\\' + file_nun[count -1] + '\\' + f)
                os.remove(fullpath)

    #         print(Word_list)
    #         print(len(Word_list))
    count = count + 1




