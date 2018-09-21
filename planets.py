def weight_on_planets():
   # write your code here
   
   #establish weight on earth and store value
   earthWeight = input("What do you weigh on earth? ")
   
   #convert earthweight to int
   weightStandard = int(earthWeight)
   
   #calculate and store other weights on Mars and Jupiter
   marsWeight = 0.38 * weightStandard
   jupiterWeight = 2.34 * weightStandard
   
   print(f"\nOn Mars you would weigh {marsWeight} pounds.\nOn Jupiter you would weigh {jupiterWeight} pounds.")
   
   
   
   
   
   
   
   
   
   
   
   
   
 
   
if __name__ == '__main__':
   weight_on_planets()