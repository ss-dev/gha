import sys
from time import sleep


if __name__ == "__main__":
    print("start: {}".format(" ".join(sys.argv[1:])))
    sleep(30)
    print("done: {}".format(" ".join(sys.argv[1:])))
