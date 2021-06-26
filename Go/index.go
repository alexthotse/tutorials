package main

import "fmt"

func main()  {
	fmt.Println("Hello World!")

	var var1 = 8 + (8*8)
	var var2 int //static typed
	var2 = 76
	var var3 float64 = 5.89580
	var var4, var5, var6 int //multiple declaration
	var var7, var8, var9 = "Dude", 19, 78.6

	fmt.Println(var1)
	fmt.Println(var2)
	fmt.Println(var3)
	fmt.Println(var4)
	fmt.Println(var5)
	fmt.Println(var6)
	fmt.Println(var7)
	fmt.Println(var8)
	fmt.Println(var9)
	fmt.Printf("var1 type is ",var1)
	fmt.Printf("\nvar1 type is %T\n",var1)
	fmt.Printf("var2 type is %T\n", var2)
	fmt.Printf("var3 type is %T\n", var3)

	/*modifying Variables*/
	/*
	var x = 6

	fmt.Println(x)

	x = 10
	pfmtPrintln(x)
	*/


	const y = 12
	fmt.Println(y)
	y =13

}

