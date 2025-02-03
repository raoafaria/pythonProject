import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Function with nested loops (original)
def compute_growth(num):
    x_val = 1
    for i in range(num):
        for j in range(num):
            x_val = x_val + 1
    return x_val


# Modified function with additional computation
def compute_growth_modified(num):
    x_val = 1
    y_val = 1
    for i in range(num):
        for j in range(num):
            x_val = x_val + 1
            y_val = i + j  # Additional operation
    return x_val, y_val


# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Measure execution time for the function
def measure_time(func, n_values):
    execution_times = []
    for num in n_values:
        start_time = time.time()
        func(num)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return np.array(execution_times)


# Fit polynomial curve (expected O(n^2))
def quadratic_fit(n_input, coef1, coef2, coef3):
    return coef1 * n_input ** 2 + coef2 * n_input + coef3


def run_menu():
    print("Select an option:")
    print("1. Run Original Function")
    print("2. Run Modified Function")
    print("3. Run Merge Sort")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        run_experiment(compute_growth, "Original Function")
    elif choice == '2':
        run_experiment(compute_growth_modified, "Modified Function")
    elif choice == '3':
        test_array = [5, 2, 4, 7, 1, 3, 2, 6]
        merge_sort(test_array)
        print(f"Sorted array: {test_array}")
    elif choice == '4':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        run_menu()


def run_experiment(func, label):
    n_values = np.array([1, 2, 3, 5, 10, 15, 20, 30, 50, 75, 100, 150, 200, 300, 500])
    execution_times = measure_time(func, n_values)

    # Fit polynomial curve
    params, _ = curve_fit(quadratic_fit, n_values, execution_times)
    coef1, coef2, coef3 = params  # Extract coefficients

    # Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(n_values, execution_times, label="Measured Time", color="red")
    plt.plot(n_values, quadratic_fit(n_values, coef1, coef2, coef3),
             label=f"Fit: {coef1:.2e}*n^2 + {coef2:.2e}*n + {coef3:.2e}", color="blue")

    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title(f"Runtime of {label}")
    plt.legend()
    plt.grid(True)
    plt.show()


# Start the menu
run_menu()
