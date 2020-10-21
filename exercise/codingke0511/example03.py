"""
用面向对象思维解决问题
"""

from example02 import Circle
def main():
    """主函数（程序执行的入口）"""
    r =  float(input('请输入游泳池的半径'))
    c1, c2 = Circle(r), Circle(r+3)
    print(f'围墙的造价{c2.calc_perimeter()*32.8:.1f}元')
    print(f'地面的造价{(c2.calc_area()-c1.calc_area())*25.5:.1f}元')

if __name__ == '__main__':
    main()














