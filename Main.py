#Jose Escobar

import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    for root, dirs, files in os.walk(path): #loop goes over files on directory and subdirectory
        for i in dirs: 
            dir_list.append(i) #adds any file found on subdirectories to the array
        for i in files: #
                file_list.append(i) #adds any file found on directory to the array
    for i in range(len(file_list)): #loop goes to the array created, which length is the number of files on the root - 1
        if classify_pic(file_list[i]) > 0.5:
            dog_list.append(file_list[i]) #creates an array and adds all files classified wit a number greater than 0.5
        else:
            cat_list.append(file_list[i]) #creates an array and adds all files classified with a number less than 0.5
    return cat_list, dog_list



def main():
    start_path = './' #starts the path of the directory
    cats, dogs = process_dir(start_path) #calls the method with the start of the directory
    print("CAT LIST:")
    print(cats)
    print("DOG LIST:")
    print(dogs)


main()

