# Line 聊天格式轉換

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #\ufeff 這是txt 或 word 偷存的，編碼要改'utf-8-sig'
        for line in f:
            lines.append(line.strip()) #移除空白符號
    return lines
       


def convert(lines):
    Allen_word_count = 0
    Allen_sticker_count = 0
    Allen_pic_count = 0
    Viki_word_count = 0
    Viki_sticker_count = 0
    Viki_pic_count = 0

    for line in lines:
        s = line.split(' ') #split 誇號中間打遇到什麼做切割，也可以是逗號 ' , '
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_pic_count += 1
            else:
                for m in s[2:]:
                    Allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == "貼圖":
                Viki_sticker_count += 1
            elif s[2] == '圖片':
                Viki_pic_count += 1
            else:
                for m in s[2:]:
                    Viki_word_count += len(m)
    print('Allen 說了', Allen_word_count,  '個字')  # 變數是數字，所以不用字串相加
    print('Allen 貼了', Allen_sticker_count,'張貼圖')
    print('Allen 傳了', Allen_pic_count,'張圖片')
    
    print('Viki 說了', Viki_word_count, '個字')
    print('Viki 貼了', Viki_sticker_count,'張貼圖')
    print('Viki 傳了', Viki_pic_count,'張圖片')



def write_file(filename, lines ):
    with open(filename, 'w') as f:  # 不用寫 encoding='utf-8'
        for line in lines:     #在一行一行的寫入
            f.write(line + '\n')

      
def main():
    lines = read_file('LINE_Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()










