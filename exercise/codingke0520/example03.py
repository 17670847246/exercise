import glob
import os
from threading import Thread

from PIL import Image

PREFIX = 'thumbnails'

def generate_thumbnail(infile, size, image_format='PNG'):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, image_format)

def main():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('images/*.jpg'):
        for size in (32, 64, 128):
            # 创建并启动线程
            Thread(
                target=generate_thumbnail,
                args=(infile, (size, size), 'JPEG')
            ).start()





if __name__ == '__main__':
    main()