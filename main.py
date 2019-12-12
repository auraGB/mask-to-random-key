import random # for the random char generation
import string #to access the alphabet easily
import re #for the split regex

mask = "xxxxx-xxxxx-xxxxx" #the mask ( how you want the randomly generated string to look like )
spliter = "-" # what will seperate the groups
mask_output = [] #list the mask will append to

def random_char():
  return random.choice(string.ascii_letters) #only ascii letters ( a - z & A - Z)

def parse():
  idx = 0 #idx for while loop counter 
  split = re.split('([^a-zA-Z0-9])', mask)
  size = len(split)
  #will loop though untill complete 
  while idx != size:
    if (spliter in split[idx]):
      #checking if the idx is the spliter which is -
      mask_output.append(spliter)
    else:
      #if its not loop though each of the charcters and replace the x varibles to a random char
      for x in split[idx]:
        mask_output.append(x.replace(x, random_char()))
      
    idx += 1 #idx increment for the while loop

#returns a string from a list
def to_string(val):
  string = ""
  for x in val:
    string += x
  return string


parse() #calling functions 
print(to_string(mask_output)) #prints out the converted list to string
