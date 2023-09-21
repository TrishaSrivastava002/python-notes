try:
    a=5/0
    b=a-5
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("NO error found")
finally:
# always runs it's used because it may be possible that try and except return a value
# and in that case any normal statement like print will not execute but "finally" will execute
    print("Cleaning up the mess")

    # how to make our own exception handler
class valuetoobig(Exception):
    pass

def test(x):
    if x>100:
        raise valuetoobig("value is to big")
    
try:
    test(200)
except valuetoobig as e:
    print(e)        