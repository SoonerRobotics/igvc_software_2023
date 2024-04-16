import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #python_log_data = np.genfromtxt("py_index_log.txt", delimiter="\n")
    cpp_log_data = np.genfromtxt("index_log_file.txt", delimiter="\n")

    indices = np.linspace(1, len(cpp_log_data), len(cpp_log_data))

    counts = np.unique(cpp_log_data, return_counts=True)

    print(counts)

    plt.scatter(indices, cpp_log_data)
    plt.show()
    print(indices)