import fileB

whatever = True

def thefunc():
    print("brute065 by @hani_j85")

while whatever == True:

    print("""
        1-md5 cracker
        2-pdf cracker
        3-zip cracker
    """)

    choice = input("Choice: ")

    if choice == "1":
        fileB.my_func()
        execfile('MD5cracker.py')


    elif choice == "2":
                fileB.my_func()
        execfile('pdf_cracker.py')



    elif choice == "3":
                         fileB.my_func()
        execfile('ZIP-Password-BruteForcer.py')

    else:
        print("... again")