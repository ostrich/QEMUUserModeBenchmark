package main

import "fmt"

const limit = 25_000_000

func primeCount(limit int) int {
	if limit < 2 {
		return 0
	}

	composite := make([]bool, limit+1)
	for i := 2; i*i <= limit; i++ {
		if !composite[i] {
			for j := i * i; j <= limit; j += i {
				composite[j] = true
			}
		}
	}

	count := 0
	for i := 2; i <= limit; i++ {
		if !composite[i] {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(primeCount(limit))
}
