"""
读写二进制文件
"""


def main():
    with open('files/zhaobaishi.jpg', mode='rb') as file, \
            open('files/赵白石.jpg', mode='wb') as file2:
            data = file.read(512)
            counter = 0
            while data:
                counter += 1
                file2.write(data)
                data = file.read(512)
                if counter > 10:
                    break


if __name__ == '__main__':
    main()


