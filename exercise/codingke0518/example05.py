"""
将列表字典写入文件
序列化： 对象 ---> 字符串 （str）/ 字节串（bytes）
反序列化 字符串/字节串 ---> 对象
处理成字符串用json,处理成字节串用pickle
"""
# JavaScript Object Notation
import json

def main():
    person = {'name': 'two', 'age': 40, 'gender': 'Male'}
    with open('files/person.txt', 'w', encoding='utf-8') as file:
        json.dump(person, file)
    with open('files/person.txt', 'r', encoding='utf-8') as file:
        result = json.load(file)
        print(type(result), result)

if __name__ == '__main__':
    main()


