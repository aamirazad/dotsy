package cmd

import (
	"github.com/spf13/cobra"
)

// initCmd represents the init command
var initCmd = &cobra.Command{
	Use:   "init",
	Short: "Create a new configuration store",
	Long: `Init (dotsy init) sets up a git repo and initializes cobra there:

The default path is ~/.dotfiles but this can be changed with the --path flag.
Dotsy will also create a config.yaml file which is where dotsy will remember
what applications are installed and their their configuration files are found.`,
	// Run: func(cmd *cobra.Command, args []string) {
	// 	fmt.Println(cfgFile)
	// },
}

func init() {
	rootCmd.AddCommand(initCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// initCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// initCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
