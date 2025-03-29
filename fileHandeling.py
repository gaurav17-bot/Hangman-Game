## way to detect file in same folder
import os
file_path="test.txt"

if os.path.exists(file_path):
    print(f"'{file_path}' exits")
else:
    print("Doesnot exists")

############ write a file ###################



text_data="Hello world"
file_path="output.txt"

with open(file_path,"w") as file:
    file.write(text_data)
    print(f"'{file_path}' was created")

    

### to write an absolute file######
text="Its an absolute file"
file_path="C:/Users/Lenovo/Videos/output.txt"
with open(file_path,"w") as file:
    file.write(text)
    print(f"'{file_path}' was created")