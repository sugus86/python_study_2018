import pyautogui
#  当前鼠标的坐标
t=pyautogui.position()
print(t)

print(pyautogui.size())

#  (x,y)是否在屏幕上
x, y = 122, 244
print(pyautogui.onScreen(x, y))

pyautogui.alert('这个消息弹窗是文字+OK按钮')

pyautogui.screenshot('foo.png')
