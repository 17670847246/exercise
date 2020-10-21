"""
打开文件 ---> open(文件路径，操作模式，字符编码）

"""


def main():
    try:
        with open('files/sye.txt', mode='a', encoding='utf-8') as file:  # gbk -> 国标库（扩展码）
            file.write('渭城朝雨浥轻尘\n')
            file.write('客舍青青柳色新\n')
            file.write('劝君更尽一杯酒\n')
            file.write('西出阳关无故人\n')
            file.close()
    except LookupError:
        print('指定了无效的编码')
    except:
        print('代码出错，联系客服')


if __name__ == '__main__':
    main()
