package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main()  {
	num := 101031433
	res := solution(num)
	fmt.Println(res)
}

func solution(num int) int {
	var valueToBeReplaced1, valueToBeReplaced2 string
	str := strconv.Itoa(num)
	startsWithOne := false
	for i, v := range str {
		if valueToBeReplaced1 == "" && v != '9' {
			valueToBeReplaced1 = string(v)
		}

		if i == 0 && v == '1' {
			startsWithOne = true
		}

		if valueToBeReplaced2 == "" && v != '1' && v != '0' {
			valueToBeReplaced2 = string(v)
		}
	}

	var maxi, mini int

	if valueToBeReplaced1 == "" {
		maxi = num
	} else {
		val, err := strconv.Atoi(strings.ReplaceAll(str, valueToBeReplaced1, "9"))
		if err == nil {
			maxi = val
		}
	}

	if valueToBeReplaced2 == "" {
		mini = num
	} else {
		replacingValue := ""
		if startsWithOne {
			replacingValue = "0"
		} else {
			replacingValue = "1"
		}
		val, err := strconv.Atoi(strings.ReplaceAll(str, valueToBeReplaced2, replacingValue))
		if err == nil {
			mini = val
		}
	}

	return maxi - mini
}

