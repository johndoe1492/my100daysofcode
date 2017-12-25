#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

a = raw_input("Enter the word ")
print a[::-1]
if a == a[::-1]:
    print "this is palindrome"
else:
    print "not a palindrome"