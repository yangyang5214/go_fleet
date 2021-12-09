package main

import (
	"fmt"
)

// 1. x 先手
// 2. len(x) >= len(o)
// 3. 连线

func validTicTacToe(boards []string) bool {
	xCount := 0
	oCount := 0

	arr := make([][]string, 3)
	for i := range arr {
		arr[i] = make([]string, 3)
	}

	for index, board := range boards {
		for i := 0; i < 3; i++ {
			v := board[i : i+1]
			if v == "X" {
				xCount++
			} else if v == "O" {
				oCount++
			}
			arr[index][i] = v
		}
	}

	//不符合出棋顺序
	if !(xCount-oCount == 0 || xCount-oCount == 1) {
		return false
	}

	if win(boards, 'X') && xCount-oCount != 1 {
		return false
	}
	if win(boards, 'O') && xCount-oCount != 0 {
		return false
	}
	return true
}

func win(board []string, p byte) bool {
	for i := 0; i < 3; i++ {
		if board[i][0] == p && board[i][1] == p && board[i][2] == p {
			return true
		}
		if board[0][i] == p && board[1][i] == p && board[2][i] == p {
			return true
		}
	}
	if board[0][0] == p && board[1][1] == p && board[2][2] == p {
		return true
	}
	if board[0][2] == p && board[1][1] == p && board[2][0] == p {
		return true
	}
	return false
}

func main() {
	//["XOX","OXO","XOX"] true
	//["XOX","O O","XOX"]  true 注意这个特殊情况，x 再下一步就赢了，所以默认值是 true,给出 false 的条件，提前终止判断
	//["O  ","   ","   "]  false
	//["XOX"," X ","   "]  false
	//["XXX", "OOX", "OOX"]  true 最后下相交的点
	//["XXX","XOO","OO "]  false
	board := []string{"XOX", "OXO", "XOX"}
	fmt.Println(validTicTacToe(board))

	board = []string{"XOX", "O O", "XOX"}
	fmt.Println(validTicTacToe(board))

	board = []string{"O  ", "   ", "   "}
	fmt.Println(validTicTacToe(board))

	board = []string{"XOX", " X ", "   "}
	fmt.Println(validTicTacToe(board))

	board = []string{"XXX", "OOX", "OOX"}
	fmt.Println(validTicTacToe(board))

	board = []string{"XXX", "XOO", "OO "}
	fmt.Println(validTicTacToe(board))

}
