package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
)

var convMap = map[string]string{
	"01": "2",
	"12": "3",
	"23": "4",
	"34": "5",
	"45": "6",
	"56": "7",
	"67": "8",
	"78": "9",
	"89": "0",
	"90": "1",
}

func doesExist(st string) (res bool) {
	_, res = convMap[st]
	return
}

func getSol2(arr []string) string {

	for index := 0; index < 10; index++ {
		interestedField := string(index) + string((index+1)%2)
		newQueue := []string{}

		fr
	}
}

// func getSol(arr []string) string {
// 	sol := []string{}
// 	loaded := ""
// 	for len(arr) > 0 {
// 		currentIndex := 0

// 		if loaded == "" {
// 			loaded = arr[currentIndex]
// 			arr = arr[1:]
// 		}

// 		if len(arr) > 0 && doesExist(loaded+arr[currentIndex+1]) {
// 			loaded = convMap[loaded+arr[0]]
// 			arr = arr[1:]
// 		} else if len(sol) > 0 && doesExist(sol[len(sol)-1]+loaded) {
// 			//pop the last from sol
// 			loaded = convMap[sol[len(sol)-1]+loaded]
// 			sol = sol[0 : len(sol)-1]
// 		} else {
// 			sol = append(sol, loaded)
// 			loaded = ""
// 		}

// 	}

// 	return strings.Join(sol, "")

// }

func formatIntoStringArray(str string) []string {
	sol := []string{}
	for _, val := range str {
		sol = append(sol, string(val))
	}

	return sol
}

type TestCase struct {
	str string
}
type Problem struct {
	T         int64
	testCases []TestCase
}

func main() {

	var problem Problem
	var index int = 0
	reader := bufio.NewReader(os.Stdin)
	for {
		line, err := reader.ReadBytes('\n')
		if err != nil {
			break
		}
		if index%2 != 0 {
			index += 1
			continue
		}
		strline := string(bytes.TrimSuffix(line, []byte("\n")))
		if problem.T == 0 {
			problem.T, err = strconv.ParseInt(strline, 10, 64)
			if err != nil {
				break
			}
		} else {
			var testCase TestCase = TestCase{
				str: strline,
			}

			problem.testCases = append(problem.testCases, testCase)

		}
		index += 1
	}
	//fmt.Println(problem)
	for index, testCase := range problem.testCases {

		ans := getSol2(formatIntoStringArray(testCase.str))
		fmt.Printf("Case #%d: %s\n", index+1, ans)
	}

}
