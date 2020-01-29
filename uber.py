def bill(kilo):
    pay=0
    if(kilo<=5):
        pay=25
        print(pay)
    else:
        pay=25+(kilo-5)*17
        print(pay)
print("1.AVADI")
print("2.KUMANCHAVADI")
print("3.IYYAPANTHANGAL")
print("4.PONNAMALLE")
a=raw_input ("enter destination")
if(a=='1'):
    print("1.AVADI")
    bill(5)
elif(a=='2'):
    print("2.KUMANCHAVADI")
    bill(7)
elif(a=='3'):
    print("3.IYYAPANTHANGAL")
    bill(8)
elif(a=='4'):
    print("4.PONNAMALLE")
    bill(10)

'''
sample input :
Enter destination: 3
sample output:
1.AVADI
2.KUMANCHAVADI
3.IYYAPANTHANGAL
4.PONNAMALLE
enter destination3
3.IYYAPANTHANGAL
76
'''
