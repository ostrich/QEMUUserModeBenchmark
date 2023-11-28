package main

import (
	"fmt"
	"math"
	"sync"
)

// PrimeSieve generates prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.
func PrimeSieve(limit uint64, wg *sync.WaitGroup, ch chan uint64) {
	defer wg.Done()

	// Create a boolean slice to represent whether each number is prime.
	isPrime := make([]bool, limit+1)
	for i := range isPrime {
		isPrime[i] = true
	}

	// 0 and 1 are not prime.
	isPrime[0], isPrime[1] = false, false

	// Iterate through the numbers up to the square root of the limit.
	for i := uint64(2); i <= uint64(math.Sqrt(float64(limit))); i++ {
		// If i is prime, mark its multiples as not prime.
		if isPrime[i] {
			for j := i * i; j <= limit; j += i {
				isPrime[j] = false
			}
		}
	}

	// Send primes to the channel.
	for i, prime := range isPrime {
		if prime {
			ch <- uint64(i)
		}
	}

	close(ch)
}

func main() {
	const limit = 1e7

	// Use a WaitGroup to wait for goroutines to finish.
	var wg sync.WaitGroup

	// Create a channel to receive prime numbers.
	ch := make(chan uint64, 1000)

	// Start the goroutine for prime sieve.
	wg.Add(1)
	go PrimeSieve(limit, &wg, ch)

	// Start a goroutine to print primes from the channel concurrently.
	go func() {
		for prime := range ch {
			fmt.Println(prime)
		}
	}()

	// Wait for the prime sieve to finish.
	wg.Wait()

}
