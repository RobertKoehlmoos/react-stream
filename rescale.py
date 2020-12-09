from random import gauss, random, seed


def rescale(data):
    # Rescale takes as input a list of numbers and rescales the list to have a
    # maximum value of 1 and a minimum value of -1
    return [i/(max(data)-min(data)) for i in data]


def normalize(data):
    # Takes as input a list of numbers and normalized the data to have
    # a mean of zero and a standard deviation of 1
    avg = sum(data)/len(data)
    variance = sum([(i - avg)**2 for i in data])/len(data)
    std_dev = variance**0.5
    return [(i - avg)/std_dev for i in data]


seed(123)  # Seeding to enable replication
to_scale = [random()*100 for _ in range(16)]
print("List to rescale: ", end="")
[print(f"{i:.2f}", end=" ") for i in to_scale]
rescaled = rescale(to_scale)
print("\nRescaled List: ", end="")
[print(f"{i:.2f}", end=" ") for i in rescaled]

to_normalize = [gauss(42, 10) for _ in range(16)]
print("\nList to normalize: ", end="")
[print(f"{i:.2f}", end=" ") for i in to_normalize]
normalized = normalize(to_normalize)
print("\nNormalized List: ", end="")
[print(f"{i:.2f}", end=" ") for i in normalized]

# Output
# C:\Users\17033\Anaconda3\envs\example_code\python.exe "C:/Users/17033/Desktop/Drive/Senior Dev/example_code/rescale.py"
# List to rescale: 5.24 8.72 40.72 10.77 90.12 3.82 53.62 33.22 85.21 15.97 33.72 33.38 24.52 0.17 43.63 8.76
# Rescaled List: 0.06 0.10 0.45 0.12 1.00 0.04 0.60 0.37 0.95 0.18 0.37 0.37 0.27 0.00 0.49 0.10
# List to normalize: 38.89 39.81 37.64 52.00 45.66 39.53 53.08 55.77 63.81 44.93 34.97 38.51 50.97 27.43 32.04 56.97
# Normalized List: -0.57 -0.48 -0.70 0.77 0.12 -0.51 0.88 1.15 1.98 0.04 -0.98 -0.61 0.66 -1.75 -1.28 1.28
# Process finished with exit code 0
