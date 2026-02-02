SHELL := /bin/bash
ARCH_FILE := architectures.txt
ARCHS := $(shell grep -v '^[[:space:]]*#' $(ARCH_FILE) | tr '\n' ' ')
BIN_DIR := bin
RESULTS_DIR := results

.PHONY: all build bench summary chart clean

all: summary chart

build:
	@mkdir -p $(BIN_DIR)
	@for arch in $(ARCHS); do \
		echo "Building for $$arch"; \
		CGO_ENABLED=0 GOOS=linux GOARCH=$$arch \
			go build -trimpath -ldflags='-s -w -extldflags "-static"' \
			-o $(BIN_DIR)/sieve.$$arch main.go || exit 1; \
	done

bench: build
	@mkdir -p $(RESULTS_DIR)
	@for arch in $(ARCHS); do \
		echo "Benchmarking for $$arch"; \
		hyperfine --shell=none -i --warmup 3 \
			--export-json $(RESULTS_DIR)/benchmark.$$arch.json \
			"./$(BIN_DIR)/sieve.$$arch" || exit 1; \
	done

summary: bench
	@python3 summary.py

chart: bench
	@python3 chart.py

clean:
	@rm -rf $(BIN_DIR) $(RESULTS_DIR) results.png
