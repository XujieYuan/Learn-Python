# Use words.txt as the file name
fh = open('words.txt')
# fname = input("Enter file name: ")
# fh = open(fname)
for line in fh:
    print(line.rstrip().upper())