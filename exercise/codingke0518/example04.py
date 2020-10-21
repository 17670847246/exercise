"""
读取网络资源保存到本地文件
URL - Universal/Uniform Resource Locator - 统一资源定位符
唯一标识网络上的一个资源 --> https://www.baidu.com:443/index.html
https://www.sohu.com:80/idxe.html

可以使用requests三方库来进行网络连接 ---> 简单好用，中文文档
pip是Python的包管理工具（联网下载/安装/卸载/更新三方库或者三方工具）
"""
import requests

# HTTP Request 向服务器发起一个请求
# HTTP Response 服务器会给浏览器一个响应
# 200 成功
# 303 重定向
# 4xx 请求有问题
# 5xx 服务器异常
def main():
    resp = requests.get('http://www.shuquge.com/txt/5809/33828003.html')
    if resp.status_code == 200:
        with open('files/yuanzun.html', 'w', encoding='utf-8') as file:
            file.write(resp.text)
    else:
        print('请求服务器发生错误')
    resp = requests.get('http://29e5534ea20a8.cdn.sohucs.com/c_zoom,h_103/c_cut,x_5,y_0,w_630,h_420/os/news/b634e1d618ffc74d3607e34eb7ec4f57.jpg')
    with open('files/赵白石.jpg', 'wb') as file:
        file.write(resp.content)


if __name__ == '__main__':
    main()


