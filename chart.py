#! /usr/bin/python3

import json
import matplotlib.pyplot as plt

# List of architectures
architectures = ["amd64", "386", "arm", "arm64", "loong64", "mips",
                 "mips64", "mips64le", "mipsle", "ppc64", "ppc64le", "riscv64", "s390x"]

# Function to process the result file for a given architecture


def process_result_file(arch):
    file_path = f'benchmark.{arch}.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
        results = data['results'][0]

        # Extract relevant information
        mean = results['mean']
        stddev = results['stddev']

        return mean, stddev


# Process each architecture and store the results
means = []
stddevs = []
for arch in architectures:
    mean, stddev = process_result_file(arch)
    means.append(mean)
    stddevs.append(stddev)

# Plotting
fig, ax = plt.subplots()

# Plot bars with error bars (standard deviation)
bars = ax.bar(architectures, means, yerr=stddevs, capsize=5)

ax.set_ylabel('Execution Time (s)')
ax.set_title('Execution Time with Standard Deviation for Each Architecture')
ax.set_xlabel('Architecture')

# Rotate x-axis labels and adjust the position of the main label
ax.set_xticklabels(architectures, rotation=45, ha='right')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin

# Add legend
# ax.legend([f'Mean ({arch})' for arch in architectures])

# Display the plot
plt.show()
