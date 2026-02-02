#!/bin/bash

ARCH_FILE="architectures.txt"
BIN_DIR="bin"

# Function to build program for a given architecture
build_for_arch() {
    arch=$1
    echo "Building for architecture: $arch"
    CGO_ENABLED=0 GOOS=linux GOARCH=$arch \
        go build -trimpath -ldflags '-s -w -extldflags "-static"' \
        -o "${BIN_DIR}/sieve.${arch}" main.go
}

mkdir -p "${BIN_DIR}"

while IFS= read -r arch; do
    [[ -z "$arch" || "$arch" =~ ^[[:space:]]*# ]] && continue
    if build_for_arch "$arch"; then
        echo "Build successful for architecture: $arch"
    else
        echo "Error building for architecture: $arch"
        exit 1
    fi
done < "${ARCH_FILE}"

echo "Build process completed successfully for all architectures"
