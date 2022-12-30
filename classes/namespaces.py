## Built-in

print(dir(__builtins__))
print(__builtins__.str.__module__)

## Globals

print(type(globals()))
print(globals())
x = "foo"
print(globals())
globals()["y"] = 100
print(globals())

## Locals
def f(x, y):
    print("Start f()")
    s = "foo"
    print(locals())
    def g():
        print("Start g()")
        
        z = "bar"
        print(locals())
        print("End g()")
    
    g()
    print(locals())
    print("End f()")

f(1, 2)
print(locals())