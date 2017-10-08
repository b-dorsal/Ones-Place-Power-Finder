# A quick script to tell if the power of a number will ever have a 0 in the ones place.
# For MAT-300 History of Mathematics
__author__ = "Brian Dorsey"
__email__ = "bdor528@gmail.com"

import os
import sys
import time

def main(argv = None):
	# hardcoded values are bad...
	starting_integer = 1
	ending_integer = 18
	starting_p = 0
	ending_p = 1000

	find_in_ones_place = '0'
	# ...but this program is just to prove one point

	found_zero = []

	start_time = time.time()

	# loop through the range of numbers to be powered
	for n in range(starting_integer, ending_integer + 1):
		# loop through each power of the number n
		for p in range(starting_p, ending_p + 1):
			n_power = n ** p
			str_n_power = str(n_power)

			# if the ones places contains the number we want, add it to the results list
			if str_n_power[len(str_n_power) - 1] == find_in_ones_place:
				str_add = str(n) + "^" + str(p) + " = " + str_n_power
				found_zero.append(str_add)
			# print str(n) + "^" + str(p) + " = " + str_n_power

	# To-Do: Make this output more readable, add "..." to clip long numbers
	# prints the results found
	print "I found ", len(found_zero), " powers with ", str(find_in_ones_place), " in the ones place. (", round((time.time() - start_time), 2), "s)"
	for f in found_zero:
		print f
	print "I found ", len(found_zero), " powers with ", str(find_in_ones_place), " in the ones place. (", round((time.time() - start_time), 2), "s)"

if __name__ == "__main__":
    sys.exit(main())