// cmd/backend/main.go
package main

import (
    "bufio"
    "fmt"
    "os"
    "os/exec"
    "path/filepath"
)

func main() {
    fmt.Println("Backend server started...")
    
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        command := scanner.Text()
        
        switch command {
        case "init":
            fmt.Println("Initializing repo...")
        //     if err := initRepo(); err != nil {
        //         fmt.Printf("Error: %v\n", err)
        //     }
        // case "quit":
            fmt.Println("Shutting down...")
            return
        default:
            fmt.Printf("Unknown command: %s\n", command)
        }
    }
}

func initRepo() error {
    homeDir, err := os.UserHomeDir()
    if err != nil {
        return fmt.Errorf("failed to get home directory: %w", err)
    }

    dotfilesPath := filepath.Join(homeDir, "dotfiles")

    // Check if directory exists
    if _, err := os.Stat(dotfilesPath); os.IsNotExist(err) {
        // Create directory
        if err := os.MkdirAll(dotfilesPath, 0755); err != nil {
            return fmt.Errorf("failed to create directory: %w", err)
        }
    }

    // Check if it's already a git repo
    if _, err := os.Stat(filepath.Join(dotfilesPath, ".git")); err == nil {
        return fmt.Errorf("git repository already exists at %s", dotfilesPath)
    }

    // Initialize git repo
    cmd := exec.Command("git", "init")
    cmd.Dir = dotfilesPath
    if err := cmd.Run(); err != nil {
        return fmt.Errorf("failed to initialize git repo: %w", err)
    }

    return nil
}
