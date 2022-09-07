import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("Name of Python script:", sys.argv[0])

# Addition of numbers
sum_of_argument = 0

for i in range(1, n):
    sum_of_argument += int(sys.argv[i])
    
print("Result:", sum_of_argument)    