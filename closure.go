package main

import "fmt"

// fibonacciGenerator returns a closure that generates Fibonacci numbers
func fibonacciGenerator() func() int {
    a, b := 0, 1
    return func() int {
        a, b = b, a+b
        return a
    }
}

func main() {
    fib := fibonacciGenerator()
    for i := 0; i < 10; i++ {
        fmt.Println(fib())
    }
}
