package main

import (
	"fmt"
	"sort"
)

func abs(x int, y int) int {
	if x > y {
		return x - y
	}
	return y - x
}

func smallestDistancePair1(nums []int, k int) int {
	r := make([]int, 0, len(nums))
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			fmt.Println(i)
			fmt.Println(j)
			fmt.Println("---")
			r = append(r, abs(nums[i], nums[j]))
		}
	}
	fmt.Println(r)
	sort.Ints(r)
	fmt.Println(r)
	return r[k-1]
}

func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	left, right := 0, nums[len(nums)-1]-nums[0]

	//二分
	for left <= right {
		mid := left + (right-left)/2

		count := 0

		//双指针，滑动窗口
		l := 0
		for r := 0; r < len(nums); r++ {
			for nums[r]-nums[l] > mid {
				l++
			}
			count = count + r - l
		}

		if count >= k {
			right = mid - 1
		} else {
			left = mid + 1
		}

	}
	return left
}

func main() {
	//nums = [1,6,1], k = 3
	//nums := []int{1, 6, 1}
	//nums := []int{1, 3, 1}
	nums := []int{38, 33, 57, 65, 13, 2, 86, 75, 4, 56} // k =>26, result => 36
	r := smallestDistancePair(nums, 26)
	fmt.Println(r)
}
