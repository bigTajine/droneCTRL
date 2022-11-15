# Read in the file
with open('drone.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('0', '1')

# Write the file out again
with open('drone.txt', 'w') as file:
  file.write(filedata)