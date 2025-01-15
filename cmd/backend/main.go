package main

import (
	"bufio"
	"fmt"
	"os"
)

// initRepo simulates a repository initialization.
func initRepo() error {
    // Implement actual repository initialization here if desired
    fmt.Println("Repository initialization logic will go here.")
    return nil
}

func main() {
    fmt.Println("Backend server started...")

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        command := scanner.Text()
        switch command {
        case "init":
            fmt.Println("Initializing repo...")
            if err := initRepo(); err != nil {
                fmt.Printf("Error: %v\n", err)
            } else {
                fmt.Println("Repository initialized successfully!")
            }
        case "quit":
            fmt.Println("Shutting down...")
            return
        default:
            fmt.Printf("Unknown command: %s\n", command)
        }
    }

    if err := scanner.Err(); err != nil {
        fmt.Fprintf(os.Stderr, "Error reading input: %v\n", err)
    }
}
