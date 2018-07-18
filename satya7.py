pp=int(raw_input())
if(pp%4==0 and pp%100!=0 or pp%400==0):
    print("leap year")
else:
    print("not a leap year")
