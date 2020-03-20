import sys
import os
import os.path
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir','-d', type=str, default='dir/', help='where to access file')
    parser.add_argument('--New_name','-name', type=str, default='NEWNAME', help='new name for rename')
    parser.add_argument('--start_number','-S_N', type=int, default=0, help='start count')
    FLAGS = parser.parse_args()

    now_dir= FLAGS.dir
    filename = os.listdir(now_dir)
    filename_ori=filename.copy()
    New_name = FLAGS.New_name
    start_number = FLAGS.start_number
    file_type = '.yaml'

    filename_begin = filename_ori[0].split('.')[0]
    filename_begin = ''.join(i for i in filename_begin if not i.isdigit())

    print("Old_name : " + filename_begin)
    print("New_name : " + New_name)

    for i in range(len(filename)):
        filename[i]=filename[i][len(filename_begin):-1*(len(file_type))]

    filename.sort(key=int)

    for i in filename:
        old_name = now_dir + filename_begin + i + file_type
        new_name = now_dir + "zzz_" + i + file_type
        os.rename(old_name, new_name)

    for i in filename:
        old_name = now_dir + "zzz_" + i + file_type
        new_name = now_dir + New_name + str(int(i) + int(start_number) - int(filename[0])) + file_type
        os.rename(old_name, new_name)
