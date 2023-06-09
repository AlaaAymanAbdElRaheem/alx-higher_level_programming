#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg_list = sys.argv
    arg_list_len = len(arg_list)
    if arg_list_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(arg_list[1])
        op = arg_list[2]
        b = int(arg_list[3])
        result = 0
        if op not in ['+', '-', '*', '/']:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = sub(a, b)
            elif op == '*':
                result = mul(a, b)
            else:
                result = div(a, b)
            print(f"{a:d} {op:s} {b:d} = {result:d}")
