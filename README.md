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
- `build.sh`: Compiles statically linked binaries for each architecture in `architectures.txt` (outputs to `bin/`).
- `benchmark.sh`: Uses [hyperfine](https://github.com/sharkdp/hyperfine) to benchmark each executable (outputs JSON to `results/`).
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
