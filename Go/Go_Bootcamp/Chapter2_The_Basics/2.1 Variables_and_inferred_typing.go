/*
Chapter 2 The Basics
2.1 Variables & inferred typing

*/ 

package main

import (
	"fmt"
)


// 2.1 Variables & inferred typing
// The var statement declares a list with the type declared last.
var (
	name string
	age int
	location string
)
// Or even
var (
	name, location string
	age int
)
// Variables can also be declared one by one:
var name string
var age int
var location string
// A var declaration can include initializers, one per variable
var (
	name string = "Prince Oberyn";
	age int = 32;
	location string = "Dorne";
)
// If an initializer is present, the type can be omitted, the variable will take the type of the initializer(inferred typing).
var (
	name = "Prince Oberyn"
	age = 32
	location = "Dorne"
)
// you can also initialize variables on the same line:
var (
	name, location, age = "Prince Oberyn", "Dorne", 32
)

// **Inside a function, the (:=) short assignment can be used in place of a var declaration with implicit type.
func main() {
	name, location := "Prince Oberyn", "Dorne"
	age := 32
	fmt.Println("%s (%d) of %s", name, age, location)
}
// A variable can contain any type, including functions:
func main() {
	action := func ()  {
		//doing something
	}
	action()
}
// Outside a function,
