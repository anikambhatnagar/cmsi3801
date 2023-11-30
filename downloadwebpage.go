package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    // Check if a URL argument is provided
    if len(os.Args) < 2 {
        fmt.Println("Usage: go run main.go <URL>")
        os.Exit(1)
    }

    // Get the URL from the command line arguments
    url := os.Args[1]

    // Send a GET request to the URL
    resp, err := http.Get(url)
    if err != nil {
        fmt.Println("Error fetching URL:", err)
        os.Exit(1)
    }
    defer resp.Body.Close()

    // Read the response body
    bodyBytes, err := io.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        os.Exit(1)
    }

    // Convert the body to a string and print it
    bodyString := string(bodyBytes)
    fmt.Println(bodyString)
}
