
# the basic syntax for opening a file in Python is:

# file = open('filename', 'mode')

# r stads for read
# w stands for write        
# a stands for append
# x stands for exclusive creation
# t stands for text mode
# b stands for binary mode

# with open('File_handeling\example.txt', 'r') as file:
#     # read the entire file
#     # print(file.readline())
#     print(file.readlines())
    
    
    
# with open('File_handeling\example.txt', 'w') as file:
#     # write to the file
#     file.write('Hello, world!\n')
#     file.write('This is a test.\n')
#     file.write('Goodbye!\n')
#     print(file.readlines())
    
    
    
# with open('File_handeling\example.txt', 'r') as file:
#     # append to the file
#     # file.write('this is line 4\n')
#     # file.write('this is line 5\n')
#     # file.write('this is line 6\n')
#     print(file.readlines())


# with open (r'File_handeling\tutorial.txt', 'x') as file:
    
#     file.write('this is a tutorial on how to create and initialize a file with some content \n')
    # read the entire file
    # print(file.readline())
    # print(file.readlines())
    
    
    

# with open(r'File_handeling\tom-barrett-hgGplX3PFBg-unsplash.jpg', "rb") as file:
#     content = file.read()
#     print(content)
    
#     file.close()
    
    
    
import os

if os.path.exists(r'File_handeling\tom-barrett-hgGplX3PFBg-unsplash.jpg'):
    print('file exists')
    os.remove(r'File_handeling\tom-barrett-hgGplX3PFBg-unsplash.jpg')
    print('file deleted')
else:
    print('file does not exist')
    
    
    
    
# os.mkdir(r'File_handeling\new_folder')

os.rmdir(r'File_handeling\new_folder')