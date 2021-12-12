package main

import (
	"fmt"
	"strings"
)

func toLowerCase(s string) string {
	var arr = make([]string, len(s))
	for index, item := range s {
		//注意限定是 A-Z [65,90]
		if item >= 'A' && item <= 'Z' {
			item = item + 32
		}
		arr[index] = string(item)
	}
	return strings.Join(arr, "")
}

func main() {
	fmt.Println(toLowerCase("al&phaBET"))
}
