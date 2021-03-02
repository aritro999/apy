base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))

print("Result:",power(base,exp))