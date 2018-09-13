import os
import shutil


root = '/home/chiendb/data/aclImdb/'


def move_file(dirin, dirout, train=True):
    dir = os.listdir(dirin)
    for file in dir:
        if train:
            file_out = file.split('_')[0] + '.txt'
        else:
            file_out = str(int(file.split('_')[0]) + 12500) + '.txt'
        shutil.move(dirin + file, dirout + file_out)


if __name__ == '__main__':
    move_file(root + 'train/pos/', root + 'pos/')
    move_file(root + 'train/neg/', root + 'neg/')
    move_file(root + 'test/pos/', root + 'pos/', False)
    move_file(root + 'test/neg/', root + 'neg/', False)
