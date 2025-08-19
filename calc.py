import sys
while True:
    print('''choose the operator to be operated with 
           + to add
           - to substract
           * to multiply
           / to divide
           # for exit ''')
    ch = input (" enter your option :- ")
    a=int(input("enter a number 1 :- "))
    b = int (input("enter a number 2 :- "))
    if ch ==  '+':
        print ( a , ch , b, "=",  a+b )
    if ch == '-' :
        print ( a , ch , b ,"=", a-b)
    if ch == '*' :
        print ( a , ch , b ,"=", a*b) 
    if ch == '/'  :
         print ( a , ch , b ,"=" ,a/b)
    if ch == '#':
        sys.exit()
    else:
        print ("ivalid option try again ")
    