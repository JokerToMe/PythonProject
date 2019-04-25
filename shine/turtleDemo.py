# 三种命令类型：
# 运动命令
# forward(d):向前移动d长度
# backward(d):向后移动d长度
# right(d) left(d) goto(x,y)
# speed(speed):范围0~10

# 笔画控制命令
# up():画笔抬起，不会再绘图
# down():画笔放下，移动会绘图
# setheading(d): 改变方向
# pensize():画笔尺寸
# pencolor()
# reset():清空窗口，重置turtle
# clear():清空窗口，不会重置turtle
# circle(r,steps=e):r为半径，e为多边形边的数量，不写时为一个圆
# begin_fill():开始填充 fillcolor(colorStr):设置填充颜色 end_fill():结束填充

# 其他命令
# done():程序继续执行 undo():撤销上一次动作
# hideturtle():隐藏海龟 showturtle():显示海龟
# screensize(x,y):设置画板大小，方法已失效

import turtle

# turtle.screensize() 
turtle.forward(100)
# 调整方向
turtle.right(45)
turtle.forward(100)
turtle.goto(-100,-200)
# 把要填充的对象对应的命令行放在fillcolor()方法之后
turtle.begin_fill()
turtle.fillcolor('red')
turtle.circle(50,steps=5)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
