import random
# to generate random numbers

# roll a random number from 0 to 11, representing the 12 zodiacs
def random_zodiac():
    return random.randint(0,11)

# run a single trial where you hatch eggs until you get 3 of the same sig
# assumption: each hatch yields the same dragon type
# returns the number of hatches needed for that trial run
def run_trial():
    # initialize an array of size 12
    # this represents how many of each zodiacs have been hatched so far
    zodiac_count = [0] * 12

    # initialize a variable to track how many hatches have been done
    num_hatches = 0

    # keep hatching until you get 3 of the same sign
    while max(zodiac_count) < 3:
        # get a random zodiac
        zodiac = random_zodiac()
        # add 1 to the zodiac_count of the zodiac you just got
        zodiac_count[zodiac] += 1
        # increment num_hatches by one
        num_hatches += 1

    # once you have 3 of the same sign, return how many hatches it took
    return num_hatches


# simulate a number of trials to get statistics on how long it takes to hatch 3 of the same sign
def simulate(num_trials = 100000):
    # initialize an array of size 26, index 0 to 25
    # the index i represents how many times you got a 3rd copy of the same sign on the ith hatch
    # note that best case is 3 and the worst case is 25
    # (if after 24 runs you get 2 of each sign, then the next one will surely be a 3rd copy  of any of the 12 signs)
    num_hatches = [0] * 26

    # repeat for a number of trials
    for _ in xrange(num_trials):
        # run a single trial
        i = run_trial()
        # update num_hatches accordingly
        num_hatches[i] += 1

    # display simulation results in a table
    print 'Number of trials: %d' % num_trials
    print '%-15s%-15s%-15s' % ('Hatches', 'Frequency', 'Probability')
    for i in xrange(3, len(num_hatches)):
        print '%-15s%-15s%-15s' % (i, num_hatches[i], float(num_hatches[i]) / float(num_trials))

    # compute average number of hatches needed (aka Expected Valud in statistics)
    print 'Average: %f' % (sum([i * float(num_hatches[i]) / float(num_trials) for i in xrange(3, len(num_hatches))]))

# run simulate()
if __name__ == '__main__':
    simulate()
