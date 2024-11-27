# Algorithm:
# 1. Define the function `fr(fn)` that takes a filename `fn` as input.
# 2. Open the file with the specified filename using `open(fn)`.
# 3. Read and print the contents of the file using `read()`.
# 4. The file is closed after the `read()` method finishes execution.

def fr(fn):
    txt = open(fn)
    print(txt.read())

fr('hello.txt')