package main

import (
	"fmt"
	"reflect"
)

func main() {
	var arr = make([]int, 10)
	arr1 := make([]int, 10)
	fmt.Println(arr)
	fmt.Println(arr1)

	//fmt.Println(arr == arr1)
	fmt.Println(reflect.DeepEqual(arr, arr1))

	m := make(map[string]int)
	m["bee"] = 20
	m["beef"] = 21
	m["beer"] = 21

	fmt.Println(m)
}
