#! /usr/bin/python3

import json
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

ARCH_FILE = Path("architectures.txt")
RESULTS_DIR = Path("results")

# Function to process the result file for a given architecture


def load_architectures():
    with ARCH_FILE.open('r') as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.lstrip().startswith("#")
        ]


def process_result_file(arch):
    file_path = RESULTS_DIR / f'benchmark.{arch}.json'
    with file_path.open('r') as file:
        data = json.load(file)
        results = data['results'][0]

        # Extract relevant information
        mean = results['mean']
        stddev = results['stddev']

        return mean, stddev


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a chart from benchmark results.')
    parser.add_argument('--output', default='results.png', help='Output image path')
    parser.add_argument('--show', action='store_true', help='Display the chart window')
    args = parser.parse_args()

    architectures = load_architectures()
    means = []
    stddevs = []
    for arch in architectures:
        mean, stddev = process_result_file(arch)
        means.append(mean)
        stddevs.append(stddev)

    fig, ax = plt.subplots()
    ax.bar(architectures, means, yerr=stddevs, capsize=5)

    ax.set_ylabel('Execution Time (s)')
    ax.set_title('Execution Time with Standard Deviation for Each Architecture')
    ax.set_xlabel('Architecture')

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.2)

    fig.savefig(args.output, dpi=150, bbox_inches='tight')
    if args.show:
        plt.show()
