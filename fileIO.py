#file io is a librery for organize data

from itertools import count


f = open('inputFile.txt', 'r')
print(f.read())
f.close()

# interect with the file by one one
f = open('inputFile.txt', 'r')
count = 0
for line in f:
    print(str(count) + line)
    count = count + 1

f.close()

#checking who pass
f = open('inputFile.txt', 'r')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

f.close()
