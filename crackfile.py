import sys

if __name__ == "__main__":
    print("Rainbow File: all")
    print("Shadow File: %s\n" % sys.argv[1])
    try:
        rainbow = open('pw\\all')
        shadow = open(sys.argv[1])
    except Exception as error:
        print(error)
        rainbow.close()
        shadow.close()

    rb_table = {}
    s_table = {}

    for line in rainbow:
        pair = line.split()
        rb_table.update({pair[0]: pair[1]})

    for line in shadow:
        line = line.strip()
        pair = line.split(":")
        s_table.update({pair[1]: pair[0]})

    for k, v in s_table.items():
        if k in rb_table.keys():
            print("Username: %16s\tPassword: %s" % (v, rb_table[k]))
        else:
            print("Username: %16s\tPassword: Not Found" % v)

    print("\nClosing Files...")
    rainbow.close()
    shadow.close()