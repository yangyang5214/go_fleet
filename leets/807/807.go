/**
例子：
输入： grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
输出： 35
解释：
The grid is:
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

从数组竖直方向（即顶部，底部）看“天际线”是：[9, 4, 8, 7]
从水平水平方向（即左侧，右侧）看“天际线”是：[8, 7, 9, 3]

在不影响天际线的情况下对建筑物进行增高后，新数组如下：

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
链接：https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline
*/

package main

import (
	"fmt"
)

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxIncreaseKeepingSkyline(grid [][]int) int {
	rowLen, colLen := len(grid), len(grid[0])
	maxRow, maxCol := make([]int, rowLen), make([]int, colLen)

	for i := 0; i < rowLen; i++ {
		for j := 0; j < colLen; j++ {
			maxRow[i] = max(maxRow[i], grid[i][j])
			maxCol[j] = max(maxCol[j], grid[i][j])
		}
	}

	fmt.Println(maxRow)
	fmt.Println(maxCol)

	result := 0
	for i := 0; i < rowLen; i++ {
		for j := 0; j < colLen; j++ {
			result = result + min(maxRow[i], maxCol[j]) - grid[i][j]
		}
	}
	return result
}

func main() {
	var grid [][]int
	grid = append(grid, []int{3, 0, 8, 4})
	grid = append(grid, []int{2, 4, 5, 7})
	grid = append(grid, []int{9, 2, 6, 3})
	grid = append(grid, []int{0, 3, 1, 0})
	fmt.Println(maxIncreaseKeepingSkyline(grid))
}
