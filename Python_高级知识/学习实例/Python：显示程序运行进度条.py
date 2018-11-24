from time import sleep
from tqdm import tqdm

import sys


'''
1、利用标准输出
    先说一下文本系统的控制符：

    \r： 将光标移动到当前行的首位而不换行；

    \n：将光标移动到下一行，并不移动到首位；

    \r\n：将光标移动到下一行首位。

示例代码如下：
'''
def viewBar(i):
    """
    进度条效果
    :param i:
    :return:
    """
    output = sys.stdout
    for count in range(0, i + 1):
        second = 0.1
        sleep(second)
        output.write('\rcomplete percent:%.0f%%' % count)
    output.flush()

viewBar(100)

'''
https://github.com/tqdm/tqdm#installation
2、tqdm模块
    tqdm是一个快速、扩展性强的进度条工具库，

    其githup地址：https://github.com/tqdm/tqdm

    （1）安装：

        直接使用pip安装：
'''

for i in tqdm(range(1, 500)):
    sleep(0.01)