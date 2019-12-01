
while True:

      #check if divisible by 3
      #A number is divisible by 3 (or 9)
      #if is internal sum is divisible by 3 (or 9)

      import winsound

      #function digit_sum
               #counts the number o f digits
               #and keep it on result

      def digit_sum(num):
            
            return sum( [ int(i) for i in str(num) ] )
            

      #input an integer x
      while True:
          try:
              x = int(input("Please enter an integer: "))
              break
          except ValueError:
               print("Error.  Enter an INTEGER.  Try again.")
               winsound.Beep(370,630)
               
               
      result = digit_sum (x)

      if result % 3 == 0:
            print()
            print (x, "is divisible by 3")
            print(x, "/ 3","=", x/3)
            winsound.Beep(1000,250) 

      else:
            print()
            print (x, "is NOT divisible by 3")
            print()
            print(x, "/ 3","=", x/3)
            winsound.Beep(370,130)


      print()
      print()
      print("{:#^42}".format("FINI"))
      print("{:-^22}".format("(c) 2019 Gil Costa"))
      print()

      

