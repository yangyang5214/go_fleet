package main

import "fmt"

func shortestCompletingWord(licensePlate string, words []string) string {
	s := make(map[int]int)
	for _, item := range licensePlate {
		flag := 0
		if item >= 97 && item <= 122 {
			flag = int(item)
		} else if item >= 65 && item <= 90 {
			flag = int(item) + 32
		}
		if flag > 0 {
			v, _ := s[flag]
			s[flag] = v + 1
		}
	}

	result := ""
	for _, item := range words {
		temps := make(map[int]int)
		for k, v := range s {
			temps[k] = v
		}
		for _, itemStr := range item {
			v, ok := temps[int(itemStr)]
			if ok {
				if v-1 == 0 {
					delete(temps, int(itemStr))
				} else {
					temps[int(itemStr)] = v - 1
				}
			}
		}
		if len(temps) == 0 {
			if len(result) == 0 {
				result = item
			} else if len(result) > len(item) {
				result = item
			}
		}
	}
	return result
}

func main() {
	//words := []string{"step", "steps", "stripe", "stepple"}
	//licensePlate := "1s3 PSt"

	words := []string{"claim", "consumer", "student", "camera", "public", "never", "wonder", "simple", "thought", "use"}
	licensePlate := "iMSlpe4"

	//words := []string{"looks", "pest", "stew", "show"}
	//licensePlate := "1s3 456"
	fmt.Println(shortestCompletingWord(licensePlate, words))
}
