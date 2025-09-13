import os


# Write to file
with open("example.txt", "w") as f:
    f.write("Hello, file!")


# Read from file
with open("example.txt", "r") as f:
    print(f.read())


# Delete the file
os.remove("example.txt")
print("File deleted!")