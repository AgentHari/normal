from package1.package1p1 import p1function1

def p1function():
    return {
        "package" : "package1",
        "file" : "p1.py",
        "function" : "p1function1",
        "des" : "This is from package2 p1.py",
        "imported" : "p1function1 from package1 > p1.py",
        "imported info" : p1function1()
    }

def needInput(in1):
    return {
        "got fron through the api" : in1
    }