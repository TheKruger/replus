import sys

def replus(a: float, b: float):
    return (a*b)/(a+b)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("usage: python3 {0} <a> <b>".format(sys.argv[0]))
        sys.exit(0)

    r = replus(float(sys.argv[2]), float(sys.argv[2]))
    print("%.2f" % r)