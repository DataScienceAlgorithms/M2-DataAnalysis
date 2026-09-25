#  Given a list of values and the number of equal-width bins to create (N),
#  write a function to return a list of the N + 1 cutoff points.

def bin_cutoff(values, n_bins):
    pass


#  Given a list of values and a list of N + 1 cutoff points,
#  write a function to return the corresponding frequencies of the N bins.

def freq_bin(values,cutoff):
    pass


if __name__ == "__main__":
    values = [18, 22, 25, 28, 30, 35, 40, 45, 50, 55]
    # number of bins
    n_bins = 3  

    cutoffs = bin_cutoff(values, n_bins)
    print(cutoffs)
    print(freq_bin(values, cutoffs))