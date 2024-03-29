﻿# QEMU User Mode Benchmarking

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
./build.sh
```
```bash
./benchmark.sh
```
```bash
./summary.py
```
```bash
./chart.py
```

## Files

- `main.go`: A [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Calculates primes up to 10 million.
- `build.sh`: Compiles statically linked binaries for each of Go's supported Linux target architectures (386, amd64, arm, arm64, loong64, mips, mips64, mips64le,mipsle, ppc64, ppc64le, riscv64, and s390x).
- `benchmark.sh`: Uses [hyperfine](https://github.com/sharkdp/hyperfine) to benchmark the execution time of each executable. Outputs results to json.
- `summary.py`: Parses json and prints results to stdout.
  - `--format text`: Default. Prints a simple table to stdout.
  - `--format csv`: Prints a CSV to stdout.
  - `--format markdown`: Prints a markdown table to stdout.
- `chart.py`: Uses [matplotlib](https://matplotlib.org/) to generate a simple chart from the json output.

## My results

Run on an AMD 5900X with 64 GiB RAM.

![Results](https://github.com/ostrich/QEMUUserModeBenchmark/blob/main/results.png?raw=true)

|Architecture|Mean (s)       |StdDev (s)     |
|----------|-----------------|-----------------|
|amd64   |0.315251|0.005368|
|386     |0.428634|0.005116|
|arm     |2.540277|0.032247|
|arm64   |1.838771|0.051209|
|loong64 |1.416593|0.027397|
|mips    |1.708859|0.034966|
|mips64  |1.541374|0.041453|
|mips64le|1.547204|0.025188|
|mipsle  |1.687246|0.038941|
|ppc64   |1.538111|0.040045|
|ppc64le |1.489758|0.023992|
|riscv64 |1.700851|0.051411|
|s390x   |1.399324|0.018790|
