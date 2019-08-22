# User input DNA sequence
try:
    DNA_sequence = input("Please enter the DNA sequence below: \n")
except:
    print("Invalid, please enter a valid DNA sequence.")
# DNA sequence to uppercases
DNA = DNA_sequence.upper()
# check for the nucleotides AT and GC and calculate the proportion
count_AT = 0
count_GC = 0
for nuc in DNA:
    if nuc == "A" or nuc == "T": # check for A or T nucleotide
        count_AT += 1
    else:   # else for G or C nucleotide
        count_GC += 1

total_nuc = count_AT + count_GC # calculate the total value of nucleotides
proportion_AT = count_AT / total_nuc # proportion AT nucleotides
proportion_GC = count_GC / total_nuc # proportion GC nucloetides

pro_AT = float("{0:.2f}".format(proportion_AT)) # proportion rounded to two decimal points
pro_GC = float("{0:.2f}".format(proportion_GC))

print("AT bases " + str(count_AT) + ", GC bases " + str(count_GC) + 
        "; Proportion AT " + str(pro_AT) + ", proportion GC " + str(pro_GC)) # print out values