def check_scope():
    def do_local():
        test = " Local test"

    def do_non_local():
        nonlocal test
        test = " Non local test"

    def do_global():
        global test
        test = " Global test"

    test = " Default"
    do_local()
    print("Test value after do local:" + test)
    do_non_local()
    print("Test value after non do local:" + test)
    do_global()
    print("Test value after do global:" + test)


check_scope()
print("Test value after main:" + test)
