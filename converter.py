num = input("enter a value : ")


print("\t1.meter\n\t2.kilometer\n\t3.centimeter")
s_num = int(input("select number : "))

if s_num == 1:
    if 'cm' in num:
        cm_num = num.replace("cm", '')
        meter = int(cm_num)/100
        print(str(meter) +"m")
    elif 'km' in num:
        k_num = num.replace("km", '')
        meter = int(k_num) * 1000
        print(str(meter) + "m")
    elif 'm' in num:
        print(num)

if s_num == 2:
    if 'c' not in num:
        me = num.replace('m', '')
        km = int(me)/1000
        print(str(km) + "km")
    elif 'c' in num:
        cm_num = num.replace("cm", '')
        km = int(cm_num) / 100000
        print(str(km) + "km")
    elif 'km' in num:
        print(num)

if s_num == 3:
    if 'k' not in num:
        m = num.replace('m', '')
        cm = int(m) * 100
        print(str(cm) + "cm")
    elif 'km' in num:
        k_num = num.replace("km", '')
        cm = int(k_num) * 100000
        print(str(cm) + "cm")
    elif 'cm' in num:
        print(num)
if s_num > 4:
    print("please enter kilo meter or meter or centimeter value")



# from unit_converter.converter import convert,converts
#
#
# num = input("enter a number")
#
# if 'min' in num:
#     a=converts(num, 'h')
#     print(a)
# if 'm' in num:
#     a=converts(num, 'km')
#     print(a)


