def plot_hist(data):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.hist(data)
    plt.title('Histogram')
    plt.xlabel('Value'); plt.ylabel('Frequency')
    plt.show()
