#coding=utf-8

import random

pom = ">"
def start():
	print u"""--------------------------------------------
		开始计算游戏吧！
--------------------------------------------
			"""

def newuser():
	name = raw_input("请输入您的姓名:".decode('utf-8').encode('gbk') + pom)
	return name

def random_new(num):
		x = random.randint(0, num)
		y = random.randint(1, num)
		return x, y
		
def add(num1, num2):
	num3 = num1 + num2
	return num3

def minus(num1, num2):
	num3 = num1 - num2
	return num3

def multiply(num1, num2):
	num3 = num1 * num2
	return num3

def division(num1, num2):
	num3 = num1 / num2
	return num3
	
start()
name = newuser()
print "\n\n\t\t欢迎%s！\n\n".decode('utf-8').encode('gbk') % name

print u"计算类型: 1、加法\n\t  2、减法\n\t  3、乘法\n\t  4、除法(舍余)\n"
calctype = raw_input("请选择计算类型".decode('utf-8').encode('gbk') + pom)
while not calctype.isdigit():
	calctype = raw_input("请选择计算类型".decode('utf-8').encode('gbk') + pom)
else:
	calctype = int(calctype)

if(calctype == 1):
	calctype = "+"
elif(calctype == 2):
	calctype = "-"
elif(calctype == 3):
	calctype = "*"
elif(calctype == 4):
	calctype = "/"
else:
	print u"输入错误，退出程序。"
	exit()

print u"\n难度: 1、初级\n      2、中级\n      3、高级"
level = raw_input("\n请选择难度".decode('utf-8').encode('gbk') + pom)
while not level.isdigit():
	level = raw_input("请选择难度".decode('utf-8').encode('gbk') + pom)
else:
	level = int(level)

if(level == 1):
	level = 10
elif(level == 2):
	level = 100
elif(level == 3):
	level = 1000
else:
	print u"输入错误，退出程序。"
	exit()

count = right = worng = 0
time = raw_input("\n请输入计算次数".decode('utf-8').encode('gbk') + pom)
while not time.isdigit():
	time = raw_input("请输入计算次数".decode('utf-8').encode('gbk') + pom)
else:
	time = int(time)

while count < time:
	x, y = random_new(level)
	print "\n%d %s %d = ?" % (x, calctype, y)
	num_input = raw_input("请输入答案".decode('utf-8').encode('gbk') + pom)
	try:
		num_input = int(num_input)
	except:
		pass
	if(calctype == "+"):
		num_sum = add(x, y)
	elif(calctype == "-"):
		num_sum = minus(x, y)
	elif(calctype == "*"):
		num_sum = multiply(x, y)
	else:
		num_sum = division(x, y)
		
	if(num_input == num_sum):
		print u"正确"
		right = right + 1
	else:
		print u"错误 %d %s %d = %d" % (x, calctype, y, num_sum)
		worng = worng + 1
	count = count + 1
else:
	print u"\n结束"
	print "姓名:%s 共完成%d题，正确%d题，错误%d题。".decode('utf-8').encode('gbk') % (name, time, right, worng)
	end = raw_input()