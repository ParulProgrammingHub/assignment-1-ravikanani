principle=input("enter principle amount : ")
time=input("enter time  in years : ")
rate=input("enter the interest rate per year in percentage : ")
def simple_interest(principle,time,rate):
    s=(principle*rate*time)/100
    return s
print "simple interest is : ",simple_interest(principle,rate,time)
