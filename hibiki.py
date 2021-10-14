#coding=utf-8
import requests
from threading import Thread
import sys
import getopt
'''requests用于请求目标站点；
threading用于启用多线程；
sys用于解析命令行参数；
getopt用于处理命令行参数；'''
# 程序标识
def banner():
    print("\n********************")
    name = '''
.__      .__  ___.     .__   __     .__ 
|  |__   |__| \_ |__   |__| |  | __ |__|
|  |  \  |  |  | __ \  |  | |  |/ / |  |
|   Y  \ |  |  | \_\ \ |  | |    <  |  |
|___|  / |__|  |___  / |__| |__|_ \ |__|
     \/            \/            \/     

    '''
    print(name)
    print("hibiki-暴力发掘器 v0.1")
    print("***********************")
# 程序用法
def usage():
    print("用法：")
    print("     -w:网址 (http://XD.com/FUZZ)")
    print("     -t:线程数")
    print("     -f:字典文件")
    print("例子：暴力发掘器.py -w http://zmister.com/FUZZ -t 5 -f commom.txt")
#创建线程并向目标站点发起请求以及获取响应
class request_performer(Thread):
    def __init__(self,word,url):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('FUZZ',self.word)#将FUZZ替换为字典
            self.url = self.urly
        except Exception as e:
            print(e)

    def run(self):
        try:
            r = requests.get(self.url)
            print(self.url,"-",str(r.status_code))
            i[0] = i[0] -1
        except Exception as e:
            print(e)
#启动request_performer()类
def launcher_thread(names,th,url):
    global i
    i = []
    resultlist = []
    i.append(0)
    while len(names):
        try:
            if i[0] < th:
                n = names.pop(0)
                i[0] = i[0]+1
                thread = request_performer(n,url)
                thread.start()
        except KeyboardInterrupt:
            print("用户停止了程序运行。完成探测")
            sys.exit()
    return True
#接收命令行中的参数将其传递给launcher_thread()函数
def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        #getopt被用来解析命令行选项参数。就不用自己写东东处理argv了。
        opts,args = getopt.getopt(sys.argv[1:],"w:t:f:")
    except getopt.GetoptError:
        print("错误的参数")
        sys.exit()
    print(opts)
    print(args)
    #opts   [('-h', ''), ('-o', 'file'), ('--help', ''), ('--output', 'out')]
    for opt,arg in opts:
        if opt == '-w':
            url = arg
        elif opt == '-f':
            dicts = arg
        elif opt == '-t':
            threads = int(arg)

    try:
        f = open(dicts,'r')
        words = f.readlines()
    except Exception as e:
        print("打开文件错误：",dicts,"\n")
        print(e)
        sys.exit()

    launcher_thread(words,threads,url)

if __name__ == '__main__':
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("用户停止了程序运行。完成探测")
