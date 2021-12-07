package usr

import (
	"fmt"
	"reflect"
)

type Hero struct {
	Name string
	Age  int
}

func changeName(hero *Hero) {
	hero.Name = "bee"
}

func noChangeName(hero Hero) {
	hero.Name = "bee"
}

func main() {
	hero := new(Hero)

	hero.Name = "beer"
	hero.Age = -1

	fmt.Println(hero)                 //&{beer -1}
	fmt.Println(reflect.TypeOf(hero)) //*main.Hero

	changeName(hero)
	fmt.Println(hero) //&{bee -1}

	var h Hero
	h.Name = "beef"
	h.Age = -2

	fmt.Println(h)                 // {beef -2}
	fmt.Println(reflect.TypeOf(h)) //main.Hero

	noChangeName(h)
	fmt.Println(h) //{beef -2}

}
