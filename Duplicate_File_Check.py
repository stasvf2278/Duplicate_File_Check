import os

def main():

    print('Enter the folder path (directory) for the first folder')             ## Enter first folder file path here
    folder1 = input()

    print('Enter the folder path (directory) for the second folder')            ## Enter second folder file path here
    folder2 = input()

    list1 = []                                                                  ## Make list for folder1
    list2 = []                                                                  ## Make list for folder2

    print(' \n \n The duplicate files are: \n')

    for root, dirs, files in os.walk(folder1):
        for file in files:
            list1.append(os.path.splitext(file)[0])

    for root, dirs, files in os.walk(folder2):
        for file in files:
            list2.append(os.path.splitext(file)[0])

    for i in list1:
        for j in list2:
            if i==j:
                print(i)

if name == "main":
    main()