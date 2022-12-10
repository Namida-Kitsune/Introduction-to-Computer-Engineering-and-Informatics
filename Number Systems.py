def binTodec():
    # 1. เลขฐานสอง แปลงเป็น เลขฐานสิบ
    user = input('กรุณาใส่เลขฐานสอง : ') [::-1]
    result = 0
    for i in range(len(user)):
        result += int(user[i]) * 2**i
    print(f'เลขฐานสอง แปลงเป็น เลขฐานสิบ : {result}')

def binTohex():
    # 2. เลขฐานสอง แปลงเป็น เลขฐานสิบหก
    user = input('กรุณาใส่เลขฐานสอง : ') [::-1]
    result = []
    full_stock = []
    stock = []
    while len(user) % 4 != 0:
        user += '0'
    for j in range(len(user)):
        stock.append(user[j])
        if len(stock) >= 4:
            full_stock.append(stock)
            stock = []
    for k in range(len(full_stock)):
        sums = 0
        for i in range(4):
            sums += int(full_stock[k][i]) * 2**i
        result.append(sums)
    result = result[::-1]
    answer = ''
    for r in result:
        if(r > 9):
            if(r == 10):
                answer += 'A'
            elif(r == 11):
                answer += 'B'
            elif(r == 12):
                answer += 'C'
            elif(r == 13):
                answer += 'D'
            elif(r == 14):
                answer += 'E'
            elif(r == 15):
                answer += 'F'
        else:
            answer += str(r)
    print(f'เลขฐานสอง แปลงเป็น เลขฐานสิบหก : {answer}')
    
def decTobin():
    # 3. เลขฐานสิบ แปลงเป็น เลขฐานสอง
    user = int(input('กรุณาใส่เลขฐานสิบ : '))
    result = ''
    while user != 0:
        result += str(user%2)
        user = user//2
    print(f'เลขฐานสิบ แปลงเป็น เลขฐานสอง : {result[::-1]}')

def decTohex():
    # 4. เลขฐานสิบ แปลงเป็น เลขฐานสิบหก
    user = int(input('กรุณาใส่เลขฐานสิบ : '))
    result = ''
    while user != 0:
        result += str(user%2)
        user = user//2
    user = result
    result = []
    full_stock = []
    stock = []
    while len(user) % 4 != 0:
        user += '0'
    for j in range(len(user)):
        stock.append(user[j])
        if len(stock) >= 4:
            full_stock.append(stock)
            stock = []
    for k in range(len(full_stock)):
        sums = 0
        for i in range(4):
            sums += int(full_stock[k][i]) * 2**i
        result.append(sums)
    result = result[::-1]
    answer = ''
    for r in result:
        if(r > 9):
            if(r == 10):
                answer += 'A'
            elif(r == 11):
                answer += 'B'
            elif(r == 12):
                answer += 'C'
            elif(r == 13):
                answer += 'D'
            elif(r == 14):
                answer += 'E'
            elif(r == 15):
                answer += 'F'
        else:
            answer += str(r)
    print(f'เลขฐานสิบ แปลงเป็น เลขฐานสิบหก : {answer}')

def hexTobin():
    # 5. เลขฐานสิบหก แปลงเป็น เลขฐานสอง
    user = input('กรุณาใส่เลขฐานสิบหก : ')
    answer = ''
    for r in user:
        if(r == '0'):
            answer += '0000'
        elif(r == '1'):
            answer += '0001'
        elif(r == '2'):
            answer += '0010'
        elif(r == '3'):
            answer += '0011'
        elif(r == '4'):
            answer += '0100'
        elif(r == '5'):
            answer += '0101'
        elif(r == '6'):
            answer += '0110'
        elif(r == '7'):
            answer += '0111'
        elif(r == '8'):
            answer += '1000'
        elif(r == '9'):
            answer += '1001'
        elif(r == 'A'):
            answer += '1010'
        elif(r == 'B'):
            answer += '1011'
        elif(r == 'C'):
            answer += '1100'
        elif(r == 'D'):
            answer += '1101'
        elif(r == 'E'):
            answer += '1110'
        elif(r == 'F'):
            answer += '1111'
    print(f'เลขฐานสิบหก แปลงเป็น เลขฐานสอง : {answer}')
    
def hexTodec():
    # 6. เลขฐานสิบหก แปลงเป็น เลขฐานสิบ
    user = input('กรุณาใส่เลขฐานสิบหก : ')
    answer = ''
    for r in user:
        if(r == '0'):
            answer += '0000'
        elif(r == '1'):
            answer += '0001'
        elif(r == '2'):
            answer += '0010'
        elif(r == '3'):
            answer += '0011'
        elif(r == '4'):
            answer += '0100'
        elif(r == '5'):
            answer += '0101'
        elif(r == '6'):
            answer += '0110'
        elif(r == '7'):
            answer += '0111'
        elif(r == '8'):
            answer += '1000'
        elif(r == '9'):
            answer += '1001'
        elif(r == 'A'):
            answer += '1010'
        elif(r == 'B'):
            answer += '1011'
        elif(r == 'C'):
            answer += '1100'
        elif(r == 'D'):
            answer += '1101'
        elif(r == 'E'):
            answer += '1110'
        elif(r == 'F'):
            answer += '1111'
    user = answer[::-1]
    result = 0
    for i in range(len(user)):
        result += int(user[i]) * 2**i
    print(f'เลขฐานสอง แปลงเป็น เลขฐานสิบ : {result}')
def select():
    yes = 1
    print("ฟังก์ชันทั้งหมด")
    print("1. เลขฐานสอง แปลงเป็น เลขฐานสิบ")
    print("2. เลขฐานสอง แปลงเป็น เลขฐานสิบหก")
    print("3. เลขฐานสิบ แปลงเป็น เลขฐานสอง")
    print("4. เลขฐานสิบ แปลงเป็น เลขฐานสิบหก")
    print("5. เลขฐานสิบหก แปลงเป็น เลขฐานสอง")
    print("6. เลขฐานสิบหก แปลงเป็น เลขฐานสิบ")
    while yes != 0:
        select = input("กรุณาเลือกฟังชัน : ")
        if(select == '1'):
            binTodec()
            yes = 0
        elif(select == '2'):
            binTohex()
            yes = 0
        elif(select == '3'):
            decTobin()
            yes = 0
        elif(select == '4'):
            decTohex()
            yes = 0
        elif(select == '5'):
            hexTobin()
            yes = 0
        elif(select == '6'):
            hexTodec()
            yes = 0
        else:
            yes = 1
select() 
    
