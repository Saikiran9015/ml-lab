import  statistics as stats
def calculate_statistics(data):
    mean = stats.mean(data)
    median = stats.median(data)
    try:
        mode = stats.mode(data)
    except stats.StatisticsError:
        mode = "No unique mode"
    return mean, median, mode

def compute_dispersion(data):
    variance = stats.variance(data)
    std_dev = stats.stdev(data)
    return variance, std_dev

def main():
    data = [13,14,15,18,19,20,25,38]
    mean, median, mode = calculate_statistics(data)
    variance, std_dev = compute_dispersion(data)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
if __name__ == "__main__":
    main()