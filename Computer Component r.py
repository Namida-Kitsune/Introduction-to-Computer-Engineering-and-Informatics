def redecimal(number):
    try:
        int(number,2)
    except:
        return False, 'ใส่ข้อมูลผิดประเภท'
    if len(number) != 8:
        return False, 'ใส่ให้มันครบ 8 ตัวสิวะ'
    else:
        return True, int(number,2)
def checksigned(number):
    if number[0] == '1':
        return redecimal(binary)[1]-256
    else:
        return redecimal(binary)[1]
while True:
    binary = input('Input 8Bit Binary: ')
    if redecimal(binary)[0]:
        print(f"Output1 natural number : {redecimal(binary)[1]}")
        print(f"Output2 signed integer : {checksigned(binary)}")
        print(f"Output3 character : {chr(redecimal(binary)[1])}")
        print(f"Output4 HEX : {hex(redecimal(binary)[1])}")
    else:
        print(f"{redecimal(binary)[1]}")
