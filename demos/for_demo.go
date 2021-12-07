package main

import (
	"fmt"
)

func main() {

	arr := []int{1, 2, 4}
	for index := range arr {
		fmt.Print(arr[index])
	}
	fmt.Println()

	for _, item := range arr {
		fmt.Print(item)
	}

	fmt.Println()

	for i := 0; i < len(arr); i++ {
		fmt.Print(arr[i])
	}

	fmt.Println()

	m := make(map[string]int)
	m["bee"] = 20
	m["beef"] = 21
	m["beer"] = 21

	for k, v := range m {
		fmt.Print(k)
		fmt.Print(": ")
		fmt.Print(v)
		fmt.Println()
	}

}
