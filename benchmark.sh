#!/bin/bash

# List of architectures
architectures=("386" "amd64" "arm" "arm64" "loong64" "mips" "mips64" "mips64le" "mipsle" "ppc64" "ppc64le" "riscv64" "s390x")

# Function to benchmark program for a given architecture
benchmark_for_arch() {
    arch=$1
    echo "Benchmarking for architecture: $arch"
    
    # Run benchmark using hyperfine
    hyperfine --shell=none -i --warmup 3 --export-json benchmark.$arch.json "./sieve.$arch"

    if [ $? -eq 0 ]; then
        echo "Benchmark successful for architecture: $arch"
    else
        echo "Error benchmarking for architecture: $arch"
        exit 1
    fi
}

# Loop through architectures and run benchmarks
for arch in "${architectures[@]}"; do
    benchmark_for_arch $arch
done

echo "Benchmarking process completed successfully for all architectures"

