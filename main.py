import os
from wsgiref.validate import validator
from file_name_validator import remove_files_ofcompletely_ignored_directory, get_invalid_file_names, get_invalid_directory_names
import logging

CHANGED_FILE_NAMES = (os.environ.get('CHANGED_FILES'))
print("CHANGED_FILE_NAMES",CHANGED_FILE_NAMES)
# FILE_NAMES_TO_IGNORE = (os.environ.get('FILE_NAMES_TO_IGNORE'))
# DIRECTORY_NAMES_TO_COMPLETELY_IGNORE = (os.environ.get('DIRECTORY_NAMES_TO_COMPLETELY_IGNORE'))
# DIRECTORY_NAMES_TO_IGNORE = (os.environ.get('DIRECTORY_NAMES_TO_IGNORE'))
# CHANGED_FILE_NAMES = ['./.github/workflows/2.yml', './1234_YOGESH_TEST_12T.py', './1234_YOGESH_TEST_12T/1234_YOGESH_TEST_12T', './1234_YOGESH_TEST_12T/1234_YOGESH_TEST_12T', './1234_YOGESH_TEST_12T/1234_YOGESH_TEST_12T']
FILE_NAMES_TO_IGNORE = ["README.md", ".gitignore", "dist", "images"]
DIRECTORY_NAMES_TO_COMPLETELY_IGNORE = [".github", "Terraform",".gitignore"]
DIRECTORY_NAMES_TO_IGNORE = ['changes', 'terraform', 'terraform-master']

file_names_to_verify = remove_files_ofcompletely_ignored_directory(CHANGED_FILE_NAMES, DIRECTORY_NAMES_TO_COMPLETELY_IGNORE)

invalid_file_names = get_invalid_file_names(file_names_to_verify, FILE_NAMES_TO_IGNORE)

invalid_directory_names = get_invalid_directory_names(file_names_to_verify, DIRECTORY_NAMES_TO_IGNORE)

if not invalid_file_names or not invalid_directory_names:
    print("hi")