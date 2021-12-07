package main

import (
	"fmt"
)


func main() {

	a := 1
	//取地址
	fmt.Println(&a)
	//取地址的值
	fmt.Println(*&a)
}
