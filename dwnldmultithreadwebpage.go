package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"sync"
)

func downloadSegment(url string, start, end int, wg *sync.WaitGroup, dataChan chan<- string) {
	defer wg.Done()

	client := &http.Client{}
	req, _ := http.NewRequest("GET", url, nil)
	rangeHeader := fmt.Sprintf("bytes=%d-%d", start, end)
	req.Header.Add("Range", rangeHeader)

	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response body:", err)
		return
	}

	dataChan <- string(bodyBytes)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <URL>")
		os.Exit(1)
	}

	url := os.Args[1]

	// Example: split the download into 4 segments
	var wg sync.WaitGroup
	dataChan := make(chan string, 4)

	for i := 0; i < 4; i++ {
		wg.Add(1)
		go downloadSegment(url, i*25, (i+1)*25-1, &wg, dataChan)
	}

	go func() {
		wg.Wait()
		close(dataChan)
	}()

	// Collect and combine data from all segments
	var data string
	for segment := range dataChan {
		data += segment
	}

	fmt.Println(data)
}
