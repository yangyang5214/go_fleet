package main

import "fmt"

func match(word, pattern string) bool {
	m := make(map[rune]byte)
	for index, item := range word {
		p := pattern[index]
		if m[item] == 0 {
			m[item] = p // 不存在就存入 index
		} else if m[item] != p {
			return false
		}
	}
	return true
}

func findAndReplacePattern(words []string, pattern string) []string {
	var r []string
	for _, item := range words {
		if match(item, pattern) && match(pattern, item) { // 颠倒判断， 类似写了两个 map
			r = append(r, item)
		}
	}
	return r
}

func ExistKey(m map[string]string, k string) bool {
	_, ok := m[k]
	if ok {
		return true
	}
	return false
}

func GetKey(m map[string]string, k string) string {
	item, ok := m[k]
	if ok {
		return item
	}
	return ""
}

func findAndReplacePattern1(words []string, pattern string) []string {
	var r []string
	for _, word := range words {
		m1 := make(map[string]string)
		m2 := make(map[string]string)
		flag := true
		for index := range word {
			w := string(word[index])
			p := string(pattern[index])
			if !ExistKey(m1, w) && !ExistKey(m2, p) {
				//如果都不存在，那就都加入map
				m1[string(word[index])] = string(pattern[index])
				m2[string(pattern[index])] = string(word[index])
				continue
			}
			if GetKey(m1, w) != p || GetKey(m2, p) != w {
				flag = false
				break
			}
		}
		if flag {
			r = append(r, word)
		}
	}
	return r
}

func main() {
	words := []string{"abc", "deq", "mee", "aqq", "dkd", "ccc"}
	pattern := "app"

	//words := []string{"ef", "fq", "ao", "at", "lx"}
	//pattern := "ya"

	r := findAndReplacePattern(words, pattern)
	fmt.Println(r)
}
