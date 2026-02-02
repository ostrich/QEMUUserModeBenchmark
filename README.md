# QEMU User Mode Benchmarking

Ever wondered which [QEMU](https://www.qemu.org/) emulator is the fastest? So did I, so I made this benchmark. It runs a [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) on each of Go's supported Linux target architectures using [QEMU User Mode Emulation](https://www.qemu.org/docs/master/user/main.html).

## Requirements

- Linux
- [QEMU](https://www.qemu.org/) with User Mode Emulation (binfmt_misc) support enabled
- [Go](https://golang.org/)
- [Python 3](https://www.python.org/)
- [hyperfine](https://github.com/sharkdp/hyperfine)
- [matplotlib](https://matplotlib.org/)

## Usage

```bash
git clone https://github.com/ostrich/QEMUUserModeBenchmark.git && cd QEMUUserModeBenchmark
```
```bash
make build
```
```bash
make bench
```
```bash
make summary
```
```bash
make chart
```

Optional: `make all` runs the full pipeline (build, bench, summary, chart).

## Files

- `main.go`: A [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Calculates primes up to 25 million and prints the count.
- `architectures.txt`: List of Go Linux target architectures to build and benchmark.
- `Makefile`: Build/benchmark pipeline. Outputs binaries to `bin/` and benchmark results to `results/`.
- `summary.py`: Parses JSON and prints results to stdout.
  - `--format text`: Default. Prints a simple table to stdout.
  - `--format csv`: Prints a CSV to stdout.
  - `--format markdown`: Prints a markdown table to stdout.
- `chart.py`: Uses [matplotlib](https://matplotlib.org/) to generate `results.png` from the JSON output.

## My results

Run on an AMD 5900X with 64 GiB RAM.

![Results](https://github.com/ostrich/QEMUUserModeBenchmark/blob/main/results.png?raw=true)

|Architecture|Mean (s)       |StdDev (s)     |
|----------|-----------------|-----------------|
|386     |0.079670|0.008981|
|amd64   |0.052152|0.006544|
|arm     |0.371544|0.018007|
|arm64   |0.323212|0.024882|
|loong64 |0.250286|0.008166|
|mips    |0.335044|0.018365|
|mips64  |0.355363|0.022990|
|mips64le|0.337094|0.011313|
|mipsle  |0.330756|0.009971|
|ppc64   |0.357804|0.015372|
|ppc64le |0.354349|0.016179|
|riscv64 |0.283564|0.013114|
|s390x   |0.526608|0.018216|
