from fileinput import filename
import re
import os
from itertools import filterfalse
changed_files = (os.environ.get('CHANGED_FILES'))
changed_file_list = changed_files.split(" ")
print("changed_file_list :", changed_file_list)
file_names_to_ignore = ["README.md", ".gitignore", "dist", "images"]
# changed_file_list = ['./.github/workflows/1.yml', './.github/workflows/script/file_name_validation.sh', './.github/workflows/test.yml', './1234_YOGESH_TEST_12T.py', './ABCD/1234_YOGESH_TEST_12T.txt']
directory_names_to_ignore_completely = [".github", "Terraform",".gitignore"]
directory_names_to_ignore_list = []

remove_dir_name_list=[]
for i in changed_file_list:
    for j in directory_names_to_ignore_completely:
        if (j in i):
            remove_dir_name_list.append(i)
changed_file_list = [i for i in changed_file_list if i not in remove_dir_name_list ]
print("CHANGED FILE LIST is After Ignored Dir name:", str(changed_file_list))

unique_file_names=[]
unique_file_name_list=[]
for i in changed_file_list:
    if (i in changed_file_list and len(changed_file_list)  != 0):
        unique_file_names = unique_file_names+changed_file_list        
        for i in unique_file_names:
            unique_file_name_list.append(i.split('/')[-1])
    else:
        print("WorkFLow RUnn Successfully")
        exit(0)
invalid_file_names=[]
file_name_list=[]
if len(unique_file_name_list) != 0:
    for file_name in unique_file_name_list:
        match = re.search("[0-9]{4}_[A-Z0-9_]*.[a-zA-Z]*$", file_name)
        print("FIlename",file_name)
        if match:
            print("valid Filename:",file_name)
        else:
            # print("Invalid FIle is :",file_name)
            file_name_list.append(file_name)
            invalid_file_names = invalid_file_names + file_name_list
            # print("invalid File Name: ", invalid_file_names)
            # os.environ["outputvar"] = file_name
            # print("Os env is :::",os.environ["outputvar"])
    if invalid_file_names:
        print("Invalid FIle :",invalid_file_names)
        exit(1)
else:
    print("WorkFLow RUnn Successfully")
    exit(0)

