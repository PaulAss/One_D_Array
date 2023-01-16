from array import *

val=array("i",[])
#Ask the user for the length of the array. The length of the array should be an integer number
len=int(input("Enter length of array: "))
for x in range(len): #Create a for loop using the array length in the range

  arr=int(input("Enter array element: "))  #Ask user to enter the array element
  val.append(arr)    #append the array element to the empty array
print(val)  #print of the array
