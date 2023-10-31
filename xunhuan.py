# -*-coding:utf-8-*-
# @Time    :2023/9/228:36
# @Author  :lizhengda
# @Email   :1055916660@qq.com
# @File    :xunhuan.py
# @Software:PyCharm

# s=eval(input("请输入数字："))
# if s%2==0:
#     print("这个数字是偶数")
# print("这个数字是:",s)
#
# s=eval(input("请输入数字："))
# if s%3==0   or s%5==0:
#     print("这个数字是15的倍数")
# else:
#     print("这个数字不能被整除的:",s)
#
# s=eval(input("请输入成绩："))
# if s>=90 and s <=100:
#     print('成绩为：A')
# elif s>=80 and s <90:
#     print('成绩为：B')
# elif s>=70 and s <=80:
#     print('成绩为：C')
# elif s>=60 and s <=70:
#     print('成绩为：D')
# elif s>=0 and s <=60:
#     print('成绩为：0')

# s = int(input("请输入成绩："))
# if s>=90 :
#     grade='A'
# elif s>=80 :
#     grade = 'B'
# elif s>=70 :
#     grade = 'C'
# elif s>=60 :
#     grade = 'D'
# else:
#     grade ="e"
# print('成绩为：0')

# for s in "hello":
#     print(s)
# inn={"name":'lisi','id':'444'}
# for s in inn:
#     print(s)
# for q in range(1):
#     print

# i=1
#
# while i < 10:
#     print(i)
#     i+= 2

# sum =0
# a=100
# while a>0:
#     sum+=a#sum=sum+a
#     a-=1#a=a-1
# print(sum)


# while True:
#     s=input("请输入姓名（按0退出）")
#     if s=="Q":
#         break
#
#     for c in s:
#         if c == "E":
#             break
#     print(c,end="") #退出for
# print('退出')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}"," ",end="")
#     print()

# print("                            _ooOoo_  ")
# print("                           o8888888o  ")
# print("                           88  .  88  ")
# print("                           (| -_- |)  ")
# print("                            O\\ = /O  ")
# print("                        ____/`---'\\____  ")
# print("                      .   ' \\| |// `.  ")
# print("                       / \\||| : |||// \\  ")
# print("                     / _||||| -:- |||||- \\  ")
# print("                       | | \\\\\\ - /// | |  ")
# print("                     | \\_| ''\\---/'' | |  ")
# print("                      \\ .-\\__ `-` ___/-. /  ")
# print("                   ___`. .' /--.--\\ `. . __  ")
# print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
# print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
# print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
# print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
# print("                            `=---='  ")
# print("  ")
# print("         .............................................  ")
# print("           佛祖镇楼                  BUG辟易  ")
# print("          佛曰:  ")
# print("                  写字楼里写字间，写字间里程序员；  ")
# print("                  程序人员写程序，又拿程序换酒钱。  ")
# print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
# print("                  酒醉酒醒日复日，网上网下年复年。  ")
# print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
# print("                  奔驰宝马贵者趣，公交自行程序员。  ")
# print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
# print("                  不见满街漂亮妹，哪个归得程序员？")

# def jj(jj,name):#
#     print(jj+name)
#
# jj('  佛祖镇楼 ','dalao')
#
# def add(a,b=2,c=5):
#     print(a+b+c)
# add(2,4,)

# def add(a,b=2,c=5):
#     result =a+b+c
#     print('佛祖镇楼 ','dalao')
#     return    result#后面的语句就不会执行了
#     print('佛祖镇楼 ','dalao')
# res =add(1,2,3,)
# print(res)

# def add(*args):
#     sum=0
#     for tt in args:
#         sum+=tt
#     print(sum)
# add(1,2,3,4,5,6,7,77)

# def add01(**kwargs):
#     print(kwargs)
# add01(a=1,b=2)

# def add(a,b=4,c=5,*args,**kwargs):
#
#     print('a',a+b+c)
#     sum =0
#     for item in args:
#         sum+= item
#     print(sum)
#     print(kwargs)
# add(1,2,3,4,5,6,x=1,y=2)

# A=66
# def add():
#     a=100
#     print(a+A)
# add()
# print(A)
# print(a)

# A=66
# def add():
#     A=100
#     print(A+A)
# add()# 打印结果166
# print(A)

A =66
def add():
    global A
    A =100
    print(A+A)
add()
print(A)

