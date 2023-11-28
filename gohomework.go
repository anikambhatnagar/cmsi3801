package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	// Check if an integer argument is provided
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run main.go <integer>")
		os.Exit(1)
	}

	// Parse the integer argument
	input, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Error: Please provide a valid integer argument.")
		os.Exit(1)
	}

	// Calculate and print perfect squares up to the given integer
	fmt.Printf("Perfect squares up to %d:\n", input)
	for i := 1; i*i <= input; i++ {
		fmt.Println(i * i)
	}
}

