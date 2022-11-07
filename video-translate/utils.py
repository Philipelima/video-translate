import validators;
import os;

def is_url(url: str):
    return validators.url(url)

def remove_file(file_name: str):
    os.remove(file_name)