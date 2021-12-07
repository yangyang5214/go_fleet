package main

import "fmt"

// 示例 1：
//
//
//输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
//输出：[[3,3],[3,2]]
//
// 示例 2：
//
//
//输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
//输出：[[1,3,3],[2,3,3]]
//
// 示例 3：
//
//
//输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
//输出：[[2,2,2],[2,1,2],[2,2,2]]

type Point struct {
	x, y int
}

func colorBorder(grid [][]int, row int, col int, color int) [][]int {
	pointers := []int{0, -1, 0, 1, 0}
	queue := []Point{{row, col}}

	//目标网格
	var result []Point

	height := len(grid)
	width := len(grid[0])

	tempColor := grid[row][col]

	recorder := make([][]bool, height)
	for i := range recorder {
		recorder[i] = make([]bool, width)
	}

	recorder[row][col] = true

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		x, y := current.x, current.y
		flag := 0

		//遍历 current 节点的 上下左右 节点
		for i := 0; i < len(pointers)-1; i++ {

			curItem := pointers[i]
			next := pointers[i+1]

			x1, y1 := x+curItem, y+next
			//判断边界 以及 颜色
			if x1 >= 0 && y1 >= 0 && x1 < height && y1 < width && grid[x1][y1] == tempColor {
				//已经被遍历过，就忽略
				if !recorder[x1][y1] {
					recorder[x1][y1] = true
					queue = append(queue, Point{x1, y1})
				}
				flag = flag + 1
			}
		}

		//找到连通节点，并且不是被包围的
		if flag > 0 && flag < 4 {
			result = append(result, Point{x, y})
		}
	}

	// 如果只有当前节点一个是 连通 的，则还是需要染色
	if len(result) == 0 {
		grid[row][col] = color
	} else {
		for _, p := range result {
			grid[p.x][p.y] = color
		}
	}

	return grid
}

func main() {
	//grid := [][]int{{1, 2, 2}, {2, 3, 2}}
	//row := 0
	//col := 1
	//color := 3
	//grid = colorBorder(grid, row, col, color)
	//fmt.Println(grid)

	//grid := [][]int{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}
	//row := 1
	//col := 1
	//color := 2
	//grid = colorBorder(grid, row, col, color)
	//fmt.Println(grid)

	grid := [][]int{{1, 1, 1, 2, 2}, {2, 1, 2, 2, 2}, {1, 1, 2, 2, 1}}
	row := 1
	col := 0
	color := 1
	grid = colorBorder(grid, row, col, color)
	fmt.Println(grid)
}
