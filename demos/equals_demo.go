package main

import (
	"./usr"
	"fmt"
	"os"
)

func main() {
	p := usr.Hero{"bee", 20}
	fmt.Println(p)

	os.Exit(-1)

	p1 := new(usr.Hero)
	p2 := new(usr.Hero)

	fmt.Println(&p1)
	fmt.Println(&p2)

	fmt.Println(p1)
	fmt.Println(p2)

	fmt.Println(p1 == p2)

	fmt.Println(*p1)
	fmt.Println(*p2)

	fmt.Println(*p1 == *p2)

}
