#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_list = sys.argv
    arg_list_len = len(arg_list)
    result = 0
    for i in range(1, arg_list_len):
        result += int(arg_list[i])
    print(f"{result:d}")
