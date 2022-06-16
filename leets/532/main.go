package main

import (
	"fmt"
	"sort"
)

//输入：nums = [3, 1, 4, 1, 5], k = 2
//输出：2
//解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
//尽管数组中有两个1，但我们只应返回不同的数对的数量。
//
//来源：力扣（LeetCode）
//链接：https://leetcode.cn/problems/k-diff-pairs-in-an-array
//著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

func findPairs(nums []int, k int) int {
	//排序
	sort.Ints(nums)
	//滑动窗口
	length := len(nums)

	r := 0
	j := 0

	pre := 0
	for i := 0; i < length; i++ { //左指针
		for j < length-1 && nums[j]-nums[i] < k {
			j++ //右指针
		}
		if i != j && nums[j]-nums[i] == k {
			if r == 0 || pre != nums[i] {
				pre = nums[i]
				r++
			}
		}
	}
	return r
}

func main() {
	fmt.Println(findPairs([]int{1}, 0) == 0)
	fmt.Println(findPairs([]int{1, 3, 1, 5, 4}, 0) == 1)
	fmt.Println(findPairs([]int{3, 1, 4, 1, 5}, 2) == 2)
	fmt.Println(findPairs([]int{1, 2, 3, 4, 5}, 1) == 4)
	fmt.Println(findPairs([]int{3, 1, 4, 1, 5}, 2) == 2)
	fmt.Println(findPairs([]int{6, 7, 3, 6, 4, 6, 3, 5, 6, 9}, 4) == 2)
}
