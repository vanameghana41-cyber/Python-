READ = 4      
WRITE = 2     
EXECUTE = 1   
file_permission = READ | WRITE   

print("File permission value:", file_permission)
if file_permission & WRITE:
    print("Write permission is set")
else:
    print("Write permission is NOT set")
#output
#File permission value: 6
#Write permission is set
