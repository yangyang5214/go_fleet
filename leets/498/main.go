package main

import (
	"fmt"
)

//硬写 m x n 行/列
// 1. 迭代的次数 m + n -1
func findDiagonalOrder(mat [][]int) []int {
	m := len(mat)
	n := len(mat[0])
	r := make([]int, 0, m*n)
	for i := 0; i < m+n-1; i++ {
		if i%2 == 0 {
			x := min(i, m-1)
			y := max(i-m+1, 0)
			for x >= 0 && y < n {
				r = append(r, mat[x][y])
				x--
				y++
			}
		} else {
			x := max(i-n+1, 0)
			y := min(i, n-1)
			for x < m && y >= 0 {
				r = append(r, mat[x][y])
				x++
				y--
			}

		}
		fmt.Println(i)
	}
	return r
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x int, y int) int {
	if x > y {
		return y
	}
	return x
}
func main() {
	var mat [][]int
	mat = append(mat, []int{1, 2, 3})
	mat = append(mat, []int{4, 5, 6})
	mat = append(mat, []int{7, 8, 9})
	r := findDiagonalOrder(mat)
	fmt.Println(r)
}
