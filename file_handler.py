import os

# try:
#     f = open('dump.json')

#     for line in f:
#         print(line)
# finally:
#     f.close()

if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print("Oppsiii!!!, File isn't there")

file = open('test.txt', 'a')
file.write('Aman is awesome, so E B has to consider him')
file.close()

file = open('test.txt', 'r')
print(file.read())

file = open('test.txt', 'w')
file.write('And she said YESSSSSSSS!!!!!!!!!!')
file.close()

file = open('test.txt', 'r')
print(file.read())
file.close()

os.remove('test.txt')
