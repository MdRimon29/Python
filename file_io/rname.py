### General way

# with open("file_io/names.txt", "r") as file:
#     lines = file.readlines()   
# for line in lines:
#     print("Hello, ", line)    # it will create like double space, like - My name is  alex\n\n

# with open("file_io/names.txt", "r") as file:
#     lines = file.readlines()   
# for line in lines:
#     print("Hello, ", line.rstrip())

### More shorter version
with open("file_io/names.txt", "r") as file:
    for line in sorted(file):
        print("My name is ", line.rstrip())