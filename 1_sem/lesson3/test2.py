# infile = open('in.txt', 'r')
#
# print(infile.readline())
#
# for line in infile:
#     print(line)
#
# infile.close()
#
#
with open('in.txt', 'r') as inf:
    with open('out.txt', 'w') as outf:
        for line in inf:
            outf.write(line)


