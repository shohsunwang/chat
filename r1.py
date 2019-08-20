# line 聊天格式轉換

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #\ufeff 這是txt 或 word 偷存的，編碼要改'utf-8-sig'
        for line in f:
            lines.append(line.strip()) #移除空白符號
    return lines
       


def convert(lines):
    new = []
    person = None  # 這範例可不加這行，但怕如果開頭不Allen，person就沒有東西，None python獨有 其他語言Null
    for line in lines:
        if line == 'Allen':
            person = 'Allen' #是用= 不是用==
            continue
        elif line == 'Tom':
            person ='Tom'   #是用= 不是用==
            continue
        if person: #person有值才運行
            new.append(person + ': ' + line) #字串連在一起是用相加，不是用逗號
    return new


def write_file(filename, lines ):
    with open(filename, 'w') as f:  # 不用寫 encoding='utf-8'
        for line in lines:     #在一行一行的寫入
            f.write(line + '\n')

      
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()
