#opens "portal" to be able to read/acces data in the file mbox-short.txt
fh = open("mbox-short.txt")
#initializes a list where usernames will be added
usernames = []

"""
the loop that reads each line of the file. Omits \n at the end of each line and looks for each line that begins with
    "Author:" and skips all the others. 
    This loop also splits the string at "@" and splits the string again at " " to extract the username only.
    The username is then appended to the list above. 
"""

for line in fh:
    clean = line.rstrip()
    if not clean.startswith("Author:"):
        continue
    username = clean.split("@")
    
    name_only = username[0].split(" ")
    usernames.append(name_only[1])

#Initialize dictionary called "name_counts"
name_counts = dict()
#for each name in usernames, this loop looks for how many times each name appears and keeps a count.
for name in usernames:
    name_counts[name] = name_counts.get(name, 0) + 1
print(name_counts)



