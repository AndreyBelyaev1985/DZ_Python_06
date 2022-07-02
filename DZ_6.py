'''
1 -  Написать программу вычисления арифметического выражения заданного строкой. 
Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
Пример: 1+2*3 => 7; (1+2)*3 => 9;

2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
Входные и выходные данные хранятся в отдельных файлах 
(в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите.
 ROT13 является примером шифра Цезаря.
Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
 Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
 Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
Не использовать функцию encode.

'''
# Задача 1 ===================
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;


Str = input("Введите пример без пробелов (Пример: 1+2*3) => ")
List = []
for i in Str:
    List.append(i)
for j in range (2):
    for i in range (len(List)):
        if i < len(List):
            if List[i] == '*':
                List[i] = int(List[i-1]) * int(List[i+1])
                List.pop(i-1)
                List.pop(i)
            elif List[i] == '/':
                List[i] = int(List[i-1]) / int(List[i+1])
                List.pop(i-1)
                List.pop(i)
        else:
            break
for j in range (2):
    for i in range (len(List)):
        if i < len(List):
            if List[i] == '+':
                List[i] = int(List[i-1]) + int(List[i+1])
                List.pop(i-1)
                List.pop(i)
            elif List[i] == '-':
                List[i] = int(List[i-1]) - int(List[i+1])
                List.pop(i-1)
                List.pop(i)
        else:
            break
print(List)


# Задача 2 ====================
# text_decoded.txt (WWWWWAAAAAAAAAAAAAAAAAAAAAAAAAWwwwwwwwBaaaaaaaWWWWWWBBBWWWWWWWWWWWWWwwwwwwwBWWWWWWWWccccccccZZZZZZZZZZZZZZZZZZZZZZZzzzzzzzzzzzzzzzzzzcc)
# text_encoded.txt (5W25A1W7w1B7a6W3B13W7w1B8W8c23Z18z2c)

with open('text_decoded.txt', 'r') as data: 
    my_File = data.read()

def rle_encode(data):
    encoding = '' 
    prev_char = ''
    count = 1 
    if not data: return ''
    for char in data: 
        if char != prev_char:
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char 
        return encoding
        
print()
encoding = rle_encode(my_File)
print(f'{encoding}\n')


with open('text_encoded.txt', 'r') as data: 
    my_File2 = data.read()

def rle_decode(data): 
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count)
            count = '' 
    return decode


decode = rle_decode(my_File2)
print(f'{decode}\n')


# Задача 3 ===========================


text = """Бал только что начался, когда Кити с матерью входила на большую, 
уставленную цветами и лакеями в пудре и красных кафтанах, залитую светом лестницу. 
Из зал несся стоявший в них равномерный, как в улье, шорох движенья, 
и, пока они на площадке между деревьями оправляли перед зеркалом прически и платья, 
из залы послышались осторожно-отчетливые звуки скрипок оркестра, начавшего первый вальс. 
Штатский старичок, оправлявший свои седые височки у другого зеркала и изливавший от себя запах духов, 
столкнулся с ними на лестнице и посторонился, видимо любуясь незнакомою ему Кити. 
Безбородый юноша, один из тех светских юношей, которых старый князь Щербацкий называл тютьками, 
в чрезвычайно открытом жилете, оправляя на ходу белый галстук, 
поклонился им и, пробежав мимо, вернулся, приглашая Кити на кадриль. 
Первая кадриль была уж отдана Вронскому, она должна была отдать этому юноше вторую. 
Военный, застегивая перчатку, сторонился у двери и, поглаживая усы, любовался на розовую Кити.
"""

def rot13(text, decode=False):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    for i in text:
        if i in alphabet:
            if decode:
                result += alphabet[(alphabet.index(i) - 13) % 33]
            else:
                result += alphabet[(alphabet.index(i) + 13) % 33]
        else:
            result += i
    return result

print('Оригинальный текст\n', text)
print('Закодированный текст\n', rot13(text))
print('Раскодированный текст\n', rot13(rot13(text), decode=True))

