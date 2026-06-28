import time
def time_it(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("Time Taken:",round(end-start,5))
    return wrapper
    @time_it
    def calc_sum():
        total=0
        for i in range(1,1000001):
         total+=1
    print("Sum:",total)
    calc_sum()