selfish ='01234567'
# 01234567 where the letters are stored in memroy, good to know for using these memory locations to index/access the string

#String Slicing [start:stop:stepover]
#[start(default=start at 0):stop(default=goto end):stepover(default=1)]
#[::-1] = print string in reverse

print(selfish[-4::])


#Immutability = Can't be changed. Stings in python are immutable

shellfish = '76543210' #This sting has now been create and allocated memory in python. From here elements of the string can't be changed unless its reassigned but this is creating a new string. So shellfish = 100 would reassign the variable shellfish with the value of integer 100 but would then remove the previous value/information from memory

#shellfish[0] = '8'     #This will produce and error = TypeError: 'str' object does not support item assignment

shellfish = '8' + shellfish #While this does add the 8 onto the string, again it isnt adding to the old sting. Its taking the old string, adding the sting value '8' to it, creating a new string also called shelfish in memeroy, and removing the old string

print(shellfish)

 

