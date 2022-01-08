#Hello thank you for using my program
#This works with Python3
#What this program do?: Copys the content from a desired file and pastes into a desired file
#How to use: python3 copy.py input.txt(the file you want to read from) output.txt(the file you want to write on)
#Thank you for using!
import sys

read_file_name = sys.argv[1]
write_file_name = sys.argv[2]
read_file = open(read_file_name, 'r')
write_file = open(write_file_name, 'w')
file_input = ""

while True:
    current_line = ""
    current_line = read_file.readline()
    if len(current_line) == 0:
        break
    file_input = file_input + current_line

write_file.write(file_input)

write_file.close()
read_file.close()
print("Your file has been copied!")
