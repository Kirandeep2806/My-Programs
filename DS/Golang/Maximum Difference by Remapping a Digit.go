package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	num := 99999
	fmt.Println(solution(num))
}

func solution(num int) int {
	str := strconv.Itoa(num)
	var valueToBeReplaced string
	for _, v := range str {
		if v != '9' {
			valueToBeReplaced = string(v)
			break
		}
	}

	var maxi string
	if valueToBeReplaced != "" {
		maxi = strings.ReplaceAll(str, valueToBeReplaced, "9")
	} else {
		maxi = str
	}

	mini := strings.ReplaceAll(str, string(str[0]), "0")
	intmaxi, _ :=  strconv.Atoi(maxi)
	intmini, _ := strconv.Atoi(mini)
	return intmaxi - intmini
}

