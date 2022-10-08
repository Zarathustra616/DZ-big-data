from count_lines import count_lines
from create_file_1mb import create_file_1mb
from multiplication import file_multiply
import time
start_time = time.time()

def main ():

    lines_count = count_lines('shagren.txt_Ascii.txt')
    create_file_1mb(lines_count)
    file_multiply(10)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
