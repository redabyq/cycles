#решил в одной написать чтобы кучу файлов не создавать
from math import sqrt, pi


#еще решил выбор заданий сделать, да, для удобства
#про аналоги Program.Main и т.д. как в С#, но в Питоне еще не знаю :)

w=1

while w!=0:
    
    w =int(input("Введите номер задания для проверки (0 для выхода): "))
    if w ==1:
    #Задача 1
        print("Задача 1")
        print("==========================")
        q=1
        n=int(input("Введите число N: "))
        while q**2<=n:
            print (q**2, end=", ")
            q=q+1        
        print("")
        
    elif w ==2:
    #Задача 2
        print("Задача 2")
        print("==========================")
        x1, x2 = int(input("Введите первое число: ")), int(input("Введите последнее число: "))
        for i in range(x1, x2+1):
            print ( "Куб %s = %s"%(i, i**3))
            
    elif w ==3:
    #Задача 3
        print("Задача 3")
        print("==========================")
        y1=int(input("Введите число: "))
        y2=int(input("Введите показатель степени: "))
        u=y1
        for i in range(1, y2):          
            u=u*y1

        print(u)
    elif w ==4:
    #Задача 4
        print("Задача 4")
        print("==========================")
        r=int(input("Введите число: "))
        c=r
        for i in range(1, r):          
            
            c=c*i

        print("%s!=%s"%(r,c))
    elif w ==5:
    #Задача 5
        print("Задача 5")
        print("==========================")
        n = int(input("Введите N до которого нужно построить последовательность Фибоначчи: ")) 
        a = 0  
        b = 1
        print(0, end=", ")
        for i in range (1, n-1): 
            c = a + b  
            a = b  
            b = c 
            print(b, end=", ")
        print("")
        
    elif w ==6:
    #Задача 6
        print("Задача 6")
        print("==========================")
        g = int(input("Введите число "))
        while g > 0:
            k = g % 10
            print(k, end=', ')
            g= g //10
        print("")

            
    elif w ==7:
    #Задача 7
        print("Задача 7")
        print("==========================")
        z = int(input("Введите число"))
        x = 0
        while z > 0:
            c = z % 10
            if x % 2 == 0:
                x += c
            z //= 10
        print(c)

    elif w ==8:
        
        v = int(input())
        b = 0
        n = 1
        while v > 0:
            m = v % 10
            b += m
            n *= m
            v //= 10
        print("Сумма равна:", b)
        print("Произведение равно:", n)
            
    else:
        print("нет такого")   















































  



