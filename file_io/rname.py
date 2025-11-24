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
# with open("file_io/names.txt", "r") as file:
#     for line in sorted(file):
#         print("My name is ", line.rstrip()) # if we want reverse order then simply just add reverse="True"
        
        
### Working on CSV
# with open("file_io/names.csv", "r") as file:
#     for line in file:
#         name, courses = line.rstrip().split(",")    #using , for seperated values in lines by comma
#         print(f"{name} takes {courses} course.")

# with open("file_io/names.csv", "r") as file:
#     for line in file:
#         name, courses = line.rstrip().split(",")    #using , for seperated values in lines by comma
#         print(f"{name} takes {courses} course.")
        
        
        
instructors=[]
with open("file_io/names.csv", "r") as file:
    for line in file:
        name, course = line.rstrip().split(",")    #using , for seperated values in lines by comma
        instructor={"name": name, "course":course}
        instructors.append(instructor)

for nm in sorted(instructors, key= (lambda student:student["name"])):
    print(f"{nm['name']} takes {nm['course']} course.")