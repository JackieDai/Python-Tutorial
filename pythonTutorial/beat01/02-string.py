
# 多行文本的形式
prragraph = '''
    这是一个段落
    可以有多个组成
'''
print(prragraph)

# 转义符 \ ; 使用 r 可以让其不转义
str1 = "123456789\n"
print(str1)

str2 = r'123456789\n'
print(str2) # 输出字符串


str = '123456789'
print(str) # 输出字符串: 123456789

print(str[0:-1]) # 输出第一个到倒数第二个的所有字符: 12345678

print(str[-9: -1])

print(str[0]) # 0

print(str[2:5]) # 345 .  (index == 2) ~ (index == 5) 但不包含 index == 5 的值

print(str[1:]) # 23456789  输出 index == 1 及其之后的字符串

print(str[0:5:2])  # 135  从 index == 0 开始，到 index == 5 结束(不包含)， step == 2

print(str*2) # 输出字符串两次  123456789123456789

print(str+"hello python") # 123456789hello python



# 字符串格式化
print("我叫 %s 今年 %d 岁!"%('jackie',10))

print("%s"%('Hello Kitty'))

print("%c"%97)
print("%c"%'a')

x = 1
print(f'{x+12}') #13

x = "hello python"
print(f'{x + ", pleasent"}')


a = "Hello World HHH"
print(a[0])

for letter in "Hello":
    print(letter)

print(a.replace("H","h",1))


def formatTest():
    # The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

    age = 36
    txt = "my age is {}"
    print(txt.format(age))

    # The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
    quantity = 3
    itemno = 567
    price = 49.95
    # myorder = "I want {} pieces of item {} for {} dollars."
    # print(myorder.format(quantity, itemno, price))
    # I want 3 pieces of item 567 for 49.95 dollars.

    # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(quantity, itemno, price))
    # I want to pay 49.95 dollars for 3 pieces of item 567.


formatTest()

a = 'qwert'
print(a.capitalize())
