#!/bin/bash

ARCH_FILE="architectures.txt"
BIN_DIR="bin"
RESULTS_DIR="results"

# Function to benchmark program for a given architecture
benchmark_for_arch() {
    arch=$1
    echo "Benchmarking for architecture: $arch"

    hyperfine --shell=none -i --warmup 3 \
        --export-json "${RESULTS_DIR}/benchmark.${arch}.json" \
        "./${BIN_DIR}/sieve.${arch}"
}

mkdir -p "${RESULTS_DIR}"

while IFS= read -r arch; do
    [[ -z "$arch" || "$arch" =~ ^[[:space:]]*# ]] && continue
    if benchmark_for_arch "$arch"; then
        echo "Benchmark successful for architecture: $arch"
    else
        echo "Error benchmarking for architecture: $arch"
        exit 1
    fi
done < "${ARCH_FILE}"

echo "Benchmarking process completed successfully for all architectures"
