package main

import "fmt"

type TopVotedCandidate struct {
	tops  []int //存储 times 对应的当前的胜出者
	times []int //存储 times 标识
}

func Constructor(persons []int, times []int) TopVotedCandidate {
	m := map[int]int{-1: -1}
	var tops []int

	top := -1
	for _, item := range persons {
		m[item] ++
		if m[item] >= m[top] {
			top = item
		}
		tops = append(tops, top)
	}
	return TopVotedCandidate{tops: tops, times: times}
}

func (this *TopVotedCandidate) Q(t int) int {
	if t <= this.times[0] {
		return this.tops[0]
	}
	for i := 0; i < len(this.times)-1; i++ {
		if t > this.times[i] && t <= this.times[i+1] {
			if this.times[i+1] == t {
				return this.tops[i+1]
			} else {
				return this.tops[i]
			}
		}
	}
	return this.tops[len(this.tops)-1]
}

func main() {

	//persons := []int{0, 1, 1, 0, 0, 1, 0}
	//times := []int{0, 5, 10, 15, 20, 25, 30}
	////0,1,1,0,0,1,0
	//
	//arr := []int{3, 12, 25, 15, 24, 8}

	//[[[0,1,0,1,1]
	//[24,29,31,76,81]]

	//[28],[24],[29],[77],[30],[25],[76],[75],[81],[80]]

	persons := []int{0, 1, 0, 1, 1}
	times := []int{24, 29, 31, 76, 81}
	arr := []int{28, 24, 29, 77, 30, 25, 76, 75, 81, 80}
	//[null,0,0,1,1,1,0,1,0,1,1]
	topVotedCandidate := Constructor(persons, times)
	for _, item := range arr {
		fmt.Printf("%d ,", topVotedCandidate.Q(item))
	}
}
