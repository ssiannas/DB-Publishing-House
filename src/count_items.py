result = []
cnt = 0
filename = input("") + ".txt"
with open("init_files\\" + filename, "r") as fp:
    for i in fp.read().splitlines():
        cnt+=1
print(cnt)


