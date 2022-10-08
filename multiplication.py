def file_multiply(Q):
    input = open('out_1mb.txt', 'r')
    output = open('out_Qmb.txt', 'a')

    content = input.readlines()

    for i in range(Q):
        for line in content:
            output.write(line)
    output.close()
    input.close()