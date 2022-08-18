# Use the file name mbox-short.txt as the file name
fh = open('mbox-short.txt')
# fname = input("Enter file name: ")
# fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    count += 1
    content = line.rstrip().split(':')
    # print(content)
    num = float(content[1])
    sum += num
avg = sum / count
print("Average spam confidence:", avg)