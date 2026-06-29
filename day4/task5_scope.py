mode="Global"
def outer():
    mode="Outer"
    def inner():
        mode="Inner"
        print("Inside Inner:",mode)
    inner()
    print("Inside Outer:",mode)
outer
print("Global:",mode)