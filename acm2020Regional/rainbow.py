# A Python3 program to find all the Stepping Number in [n, m]
 
# This function checks if an integer n is a Stepping Number
def isStepNum(n):
   
    # Initalize prevDigit with -1
    prevDigit = -1
 
    # Iterate through all digits of n and compare difference
    # between value of previous and current digits
    while (n):
       
        # Get Current digit
        curDigit = n % 10
 
        # Single digit is consider as a
        # Stepping Number
        if (prevDigit == -1):
            prevDigit = curDigit
        else:
           
            # Check if absolute difference between
            # prev digit and current digit is 1
            if (abs(prevDigit - curDigit) == 0):
                return False
        prevDigit = curDigit
        n //= 10
    return True
 
# A brute force approach based function to find all
# stepping numbers.
def displaySteppingNumbers(n, m):
   
    # Iterate through all the numbers from [N,M]
    # and check if its a stepping number.
    count = 0
    for i in range(n, m + 1):
        if (isStepNum(i)):
            count += 1
    return count
 
# Driver code
if __name__ == '__main__':
    n, m = 1, 123456789
 
    # Display Stepping Numbers in
    # the range [n, m]
    print(displaySteppingNumbers(n, m))
 
# This code is contributed by mohit kumar 29

