# 清單分割法
# 字串也可以當成清單來分割
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]  # 字串也可以當成清單來分割
    name = s[0][5:]  #前面是字串清單的位置，後面是裡面的第幾個字範圍
    print(time, name)
    print(time)
    print(name)