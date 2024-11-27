# Algorithm:
# 1. Open the file "ello.txt" in write mode ('w') and write a string to it.
# 2. Close the file after writing.
# 3. Reopen the file "ello.txt" in read mode ('r') and print its contents.

hehe = open("ello.txt", "w")  # Open file in write mode
hehe.write("Hehe I Can See You :)")  # Write a string to the file
hehe.close()  # Close the file after writing

hehe = open("ello.txt", "r")  # Open file in read mode
print(hehe.read())  # Read and print the content of the file