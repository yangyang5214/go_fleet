package main

import "strings"

func main() {
	println(truncateSentence("Hello how are you Contestant", 7))
}

func truncateSentence(s string, k int) string {
	strs := strings.Split(s, " ")
	if len(strs) > k {
		strs = strs[:k]
	}
	return strings.Join(strs, " ")
}
