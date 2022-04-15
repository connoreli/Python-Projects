

f = open('myfile.txt', 'w')
f.write('Stay tuned for our amazing summer sale!')
f.close()

f = open('myfile.txt', 'r')
print(f.read())
