# This script was used to compute the reversibility score of the most common binomials in the National Corpus of Polish
# and show the result of the computation in a separate csv file.
# I believe it to be useful for computing reversilibity score of binomials in any other corpus,
# provided that the input file contains the data in similar order:

import sys

inputfile = 'binomials_NKJP.csv'
# The input file containts the list of the most frequent binomials in the National Corpus of Polish
# Each line contains the first and the second element of a binomial, as well as its frequency and the frequency of this binomial in the reverse order
# eg. kobieta, mężczyzna, 1011, 606 [ang. woman, man, 1011, 606]

mainfile = open(inputfile, 'r')

# The reversibility score is based on a computation proposed by Sandra Mollin in 'Revisiting binomial order in English' (2012)
# The reversibility score is as follows: reversibility = [freq / (freq + revfreq)] × 100,
# with 'freq' representing the frequency of the more frequent binomial order 
# and 'revfreq' representing the frequency of the less frequent binomial order (Mollin 2012, p. 84)
# For an example given above ('woman and man', in Polish: 'kobieta i mężczyzna') the reversibility score is 62.52% (1011/(1011+606) x 100)

binomials = []

# Mollin has proposed four main categories of the reversibility of binomials:
# irreversible - with the reversibility score of 100%
irreversible = []
# reversible with a strong preference for one order (90–99.99%)
strong = []
# reversible with a moderate preference for one order (75–89.99%)
moderate = []
# reversible (50–74.99%)
reversible = []

for k in mainfile:
    element = k.split(', ')
    # We need to split each line on five elements: first element of a binomial, second one, freq, revfreq, and reversibility score
    freq = int(element[2])
    revfreq = int(element[3])
    revscore = float("{:.2f}".format((freq/(freq+revfreq))*100))
    binomials.append([element[0], element[1], freq, revfreq, revscore])
    if revscore == 100.0:
        irreversible.append(revscore)
    elif revscore < 100.0 and revscore >= 90.0:
        strong.append(revscore)
    elif revscore < 90 and revscore >= 75.0:
        moderate.append(revscore)
    else:
        reversible.append(revscore)


# Now we have a list of all binomials, with the reversibility score as the fifth element of each line
# We can save it in the output file:
outputfile = 'reversibility_NKJP.csv'
savefile = open(outputfile, 'w')

for b in binomials:
    savefile.write(b[0] + ', ' + b[1] + ', ' + str(b[2]) + ', ' + str(b[3]) + ', ' + str(b[4]) + '\n')


# We also have the separate lists of irreversibile, strong, moderate and reversibile binomials in separate lists
# We can now print the number of binomials of each type
irreversible_number = len(irreversible)
strong_number = len(strong)
moderate_number = len(moderate)
reversible_number = len(reversible)

print(irreversible_number)
print(strong_number)
print(moderate_number)
print(reversible_number)

# To calculate the percentage of each type of binomials in relation to the number of all binomials we can do the following:
binomials_number = len(binomials)

howirreversible = irreversible_number*100/binomials_number
howstrong = strong_number*100/binomials_number
howmoderate = moderate_number*100/binomials_number
howreversible = reversible_number*100/binomials_number

print(howirreversible)
print(howstrong)
print(howmoderate)
print(howreversible)

sys.exit()

mainfile.close()