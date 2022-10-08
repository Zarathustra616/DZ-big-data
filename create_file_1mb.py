import random

def create_file_1mb(lines_count):
    file = open('out_1mb.txt', 'a')
    og_file = open('shagren.txt_Ascii.txt', 'r')
    content = og_file.readlines()

    maxsize = 1048576

    while file.tell() <= maxsize:
        file.write(content[random.randrange(lines_count)])







