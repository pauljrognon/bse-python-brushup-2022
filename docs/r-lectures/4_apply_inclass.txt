# 0. Simulation ---------
set.seed(42)
# Create a matrix where:
#  - Each row represents a runner i
#  - Each column represents a race j
#  - The (i,j)-entry is N(mu_i, 0.2^2), and mu_i is N(10.5,0.1^2). 

# YOUR CODE


# Create a matrix where:
#  - Each row represents a runner i 
#  - Each column represents a race j 
#  - The (i,j)-entry is N(mu_i, 0.2^2) with probability p = 0.8, 
# and with probability p = 0.2 is NA. 

# YOUR CODE

# 1. Simple ranking ----------------
# Get the name of the winner of each race 
# (Hint: use names() and which.min())

# YOUR CODE

# Get a ranking of runners based on their number of wins
# (Hint: use table() and sort it)

# YOUR CODE

# 2. Advanced ranking -------------
# Build a function that given a named vector, 
# it returns the names of the top 3 Runners.

# YOUR CODE

# Apply this function to every race

# YOUR CODE

# Assign 5 points to the winner, 3 to the runner up, 
# and 1 to the third one in a dataframe format.

# YOUR CODE

# Apply this function to each race to obtain a list of dataframes.

# YOUR CODE

# Use rbind recursively to combine these into a single dataframe

# YOUR CODE

# Use the aggregate function to get the total points by Runner:

# YOUR CODE

# 3. Expand Grid ------------
# Generate y = Xb + e, 
# where X is n x 2 (uniform draws), b_true is 2 x 1,
# and e is N(0,1). 
# Compute the beta that minimizes mean square error by using
# expand.grid().

# Create the MSE function

# YOUR CODE

# Use expand.grid() to compute the combinations

# YOUR CODE

# Compute MSE for each combo and add it as a column

# YOUR CODE

# Return the betas with lowest MSE

# YOUR CODE
