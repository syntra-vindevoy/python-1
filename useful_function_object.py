def do_something():
    print("I'm doing something")


do_something()

ds = locals()["do_something"]
ds()

ds = globals()["do_something"]
ds()
