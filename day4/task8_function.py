def require_positive(func):
    def wrapper(a,b):
        if a>0 and b>0:
            return func(a,b)
        else:
            print("Error:Both Number are Positive")
        return wrapper
    @require_positive
    def divide(a,b):
        print("Division Result=",a/b)
    divide(4,5)
    divide(-2,5)