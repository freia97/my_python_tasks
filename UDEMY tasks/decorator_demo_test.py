def dec_func(org_func):
    def wrap():
        print("before")
        org_func()
        print("after")
    return wrap()

@dec_func
def hi():
    print("hi")