/*
Copyright © 2025 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var cfgFile string

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "dotsy",
	Short: "A command line linux config manager",
	Long: `Dotsy, the first app you run on your computer:

Dotsy is CLI tool which stores the configs of all your apps and allows you to restore them and quickly deploy them on new machines.
It provides a simple and intuitive interface to backup, restore, and deploy your configurations.`,
	// Run: func(cmd *cobra.Command, args []string) {
	// 	viper.ReadInConfig()
	// },
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	err := rootCmd.Execute()
    fmt.Println("test")

	if err != nil {
		os.Exit(1)
	}
}

func init() {
	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.

	// rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.dotsy.yaml)")

	// Cobra also supports local flags, which will only run
	// when this action is called directly.

	rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.cobra.yaml)")

}
