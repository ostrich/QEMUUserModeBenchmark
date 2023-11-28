#!/bin/bash

# List of architectures
architectures=("386" "amd64" "arm" "arm64" "loong64" "mips" "mips64" "mips64le" "mipsle" "ppc64" "ppc64le" "riscv64" "s390x")

# Function to build program for a given architecture
build_for_arch() {
    arch=$1
    echo "Building for architecture: $arch"
    CGO_ENABLED=0 GOOS=linux GOARCH=$arch go build -o sieve.$arch -ldflags '-extldflags "-static"' main.go

    if [ $? -eq 0 ]; then
        echo "Build successful for architecture: $arch"
    else
        echo "Error building for architecture: $arch"
        exit 1
    fi
}

# Loop through architectures and build
for arch in "${architectures[@]}"; do
    build_for_arch $arch
done

echo "Build process completed successfully for all architectures"

