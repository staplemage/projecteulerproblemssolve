largestFac = 2 # start on smallest prime
numLarge = 600851475143 # big number
listofPrimes = []

while (numLarge > 1): # while it hasn't been reduced
    while (numLarge % largestFac == 0): # while it fits
        listofPrimes.append(largestFac) # add to list
        numLarge /= largestFac # adjust large number
    largestFac += 1 # check next number

print(max(listofPrimes))