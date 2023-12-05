package main

import (
    "fmt"
    "os"
    "strconv"
)

// Function to calculate and print perfect squares up to a given number.
func printPerfectSquares(limit int) {
    fmt.Println("Perfect squares up to", limit, ":")
    for i := 1; i*i <= limit; i++ {
        fmt.Println(i*i)
    }
}

func main() {
    // Check if an argument is provided.
    if len(os.Args) < 2 {
        fmt.Println("Please provide an integer as an argument.")
        os.Exit(1)
    }

    // Convert the argument to an integer.
    limit, err := strconv.Atoi(os.Args[1])
    if err != nil {
        fmt.Println("Invalid input. Please provide an integer.")
        os.Exit(1)
    }

    // Calculate and print the perfect squares.
    printPerfectSquares(limit)
}
