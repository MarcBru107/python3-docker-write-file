import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

f = open("data/File.txt", "w")   # 'r' for reading and 'w' for writing
f.write("\nNew Line")
f.close()