
# Oprning file in python.

# Use open() function to open a file.
# The open() function takes two parameters; filename, and mode.
# The mode can be read, write, append, x:excluive creation(fail of file exists.) b:binary(rb, wb for
# working with the files.) + : To combine with other modes( r+ , w+ allow both reading and writing).

# Opening file in writing moode.
file = open("new_file.txt", "w")

file.write("Hello, world!\n")
file.write("This is another line.\n")
file.close()

lines = ["Lines 1: Karachi\n"]
file = open("new_file.txt", "a")
file.writelines(lines)
file.close()

# Opening file in reading mode.

file = open("new_file.txt", "r")
content = file.read()
print(content)

# prompt: generatie a comprehensive example of file handling.
# Create a file and write to it.
with open("example.txt", "w") as f:
    f.write("This is line 1.\n") 
    f.write("This is line 2.\n") 
    f.write("This is line 3.\n") 
    f.write("This is line 4.\n")
# cannot pass 2 arguments at a time.
#     f.writelines("This is line 5.\n", "This is line 6.\n") # This will raise an error.
#     f.writelines(["This is line 5.\n", "This is line 6.\n"])
    
# Read the file and print its contents.
with open("example.txt", "r") as f:
    content = f.read()
    print("---Full Content---")
    print(content)
    
# Read the file line by line and print each line.
with open("example.txt", "r")as f:
    print("---Line by Line---")
    for Line in f:
        print(Line, end='')
        
# Read a single lines.
with open("example.txt", "r" )as f:
    print("\n---Readlines---")
    print(f.readlines(), end='')
    
# Read all lines into a list.
with open("example.txt", "r")as f:
    lines = f.readlines()
    print("\n---Readlines---")
    for line in lines:
        print(line, end='')
        
# Append to the file.
with open("example.txt", "a")as f:
    f.write("This is an appended line 1.\n")
    f.write("This is an appended line 2.\n")
    
# Read with seek and tell.
with open("example.txt", "r")as f:
    print("\n---Seek and Tell---")
    print("Current position:", f.tell())
    print("First line:", f.readline(), end='')
    print("Current position:", f.tell())
    f.seek(0)
    print("After seek(0):", f.tell())
    print("First line again:", f.readline(), end='')
    
# Demonstrating 'x' mode (exclusive creation).
try:
    with open("example.txt", "x")as f:
        f.write("This is a new file created in 'x' mode")
        print("File created successfully.")
except FileExistsError:
    print("File 'new_file.txt' already exists!.")
    
# Copy file example.
def copy_file(source, destination):
    try:
        with open(source, "r")as src,  open(destination, "w")as dest:
            for line in src:
                dest.write(line)
                print(f"'{source}' successfully copied to '{destination}'")
    except FileNotFoundError:
        print(f"Error: File not found '{source}'")
    except Exception as e:
        print(f"Error during file copy: {e}")
        
copy_file("example.txt", "copy_of_example.txt")
        













































