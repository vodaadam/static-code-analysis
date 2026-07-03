#!/usr/bin/env python3

import argparse
import sys


def generate_cpp_file(depth, filename="chained_calls.cpp"):
    with open(filename, "w") as f:
        f.write("#include <cstdlib>\n\n")

        f.write("void fun0(int *ptr) {\n")
        f.write("    free(ptr);\n")
        f.write("}\n\n")

        for i in range(1, depth + 1):
            f.write(f"void funs{i}(int *ptr) {{\n")
            f.write(f"    funs{i - 1}(ptr);\n")
            f.write("}\n\n")

        f.write("int main() {\n")
        f.write("    int *my_ptr = (int*)malloc(sizeof(int));\n")
        f.write(f"    funs{depth}(my_ptr);\n")
        f.write("    free(my_ptr);\n")
        f.write("    return 0;\n")
        f.write("}\n")

    print(f"File {filename} has been created")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator of deep chained C++ function calls")
    parser.add_argument("depth", type=int, help="Depth, e.g. 1000")
    args = parser.parse_args()

    if args.depth < 1:
        print("Depth must be positive")
        sys.exit(1)

    generate_cpp_file(args.depth)