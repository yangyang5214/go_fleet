package main

import (
	"fmt"
	"strings"
)

func FindOcurrences(text string, first string, second string) []string {
	var result []string
	arrs := strings.Split(text, " ")
	for i := 0; i < len(arrs)-2; i++ {
		if arrs[i] == first && arrs[i+1] == second {
			result = append(result, arrs[i+2])
		}
	}
	return result
}

func main() {
	text := "we will we will rock you"
	first := "we"
	second := "will"
	fmt.Print(FindOcurrences(text, first, second))
}
