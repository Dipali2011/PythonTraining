"""
def accept_arg(function_to_decorator):
    def inner(*args,**kwargs):
        print("positive arguments",args)
        print("the key arguments",kwargs)
        function_to_decorator(*args)
    return inner

@accept_arg
def function_with(a,b,c):
    print(a,b,c)

function_with(10,20,30)"""

"""
def accept_arg(function_to_decorator):
    def inner(*args,**kwargs):
        print("positive arguments",args)
        print("the key arguments",kwargs)
        function_to_decorator(*args,**kwargs)
    return inner

@accept_arg
def function_with(*args,**kwargs):
    print(args)
    print(kwargs)

function_with(1,2,3,name="dipali",add="mayur park")"""
"""
def decorator_with_args(dun1,dun2,dun3):
    def decoator(func):
        def wrapper(fun1,fun2,fun3):
            print("the wrappercan access all the variables\n"
                  "\t from the decorator maker:{0},{1},{2}\n"
                  "and pass them into decorator".format(dun1,dun2,dun3,fun1,fun2,fun3))
            return func(fun1,fun2,fun3)
        return wrapper
    return decoator

panda="panda"
@decorator_with_args(panda,"numpy","ski")
def actual(fun1,fun2,fun3):
    print("this is decorator fun and it only know about its arg  {0},{1},{2}".format(fun1,fun2,fun3))

actual("john","manju","ch")"""
#chaining of decor
"""
def decor2(fun):
    def inner():
        x= fun()
        print("x in decor2",x)
        return x**2
    return inner
def decor1(fun):
    def inner():
        x= fun()
        print("x in decor2",x)
        return x*x
    return inner
def decor(fun):
    def inner():
        x=fun()
        print("x in decor 1 st",x)
        return 2+x
    return inner
@decor2
@decor1
@decor
def num():
    return 20

num()
"""


"""
data = {}
with open("annual.csv") as b, open("data-writes.txt", "w+") as w:
    pricelist = []
    for rec in b:
        rec = rec.strip()
        cols = [x.strip('"') for x in rec.split(',')]
        if cols[2] == "Open" or cols[2] == "High":
            continue
        if cols[1] in data:
            data[cols[1].strip()].append(float(cols[2]))
        else:
            data[cols[1].strip()] = [float(cols[2])]
    for year in data:
        avg_price = round(sum(data[year]) / len(data[year]), 2)
        w.write("Avg price for {} is {} \n".format(year, avg_price))


data = {}
with open("annual.csv") as b:
    pricelist = []
    for rec in b:
        rec = rec.strip()
        cols = [x.strip('"') for x in rec.split(',')]
        if cols[2] == "Open" or cols[2] == "High":
            continue
        if cols[1] in data:
            data[cols[1].strip()].append(float(cols[2]))
        else:
            data[cols[1].strip()] = [float(cols[2])]

for year in data:
    print("Average price for {} is {}".format(year, round(sum(data[year]) / len(data[year]), 2)))

"""