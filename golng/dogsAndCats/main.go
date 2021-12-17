package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

type TestCase struct {
	queue        string
	dogFoodStock Int
	catFoodStock Int
	bonusCatFood Int
}

type Problem struct {
	T         Int
	testCases []TestCase
}

func getIntValue(str string) Int {
	n, err := strconv.ParseInt(str, 10, 64)
	if err != nil {
		return -1
	}
	return Int(n)
}

func PrintOutput(problem Problem) {
	for index, testCase := range problem.testCases {
		var s string
		if IsFeedingPossible(testCase.queue, testCase.dogFoodStock, testCase.catFoodStock, testCase.bonusCatFood) {
			s = "YES"
		} else {
			s = "NO"
		}
		fmt.Printf("Case #%d: %s\n", index+1, s)

	}
}
func main() {
	// fmt.Println(IsFeedingPossible("CCDCDD", 10, 4, 0))
	// fmt.Println(IsFeedingPossible("CCCC", 1, 2, 0))
	// fmt.Println(IsFeedingPossible("DCCD", 2, 1, 0))

	// fmt.Println(IsFeedingPossible("CDCCCDCCDCDC", 4, 2, 2))
	// fmt.Println(IsFeedingPossible("DCCCCCDC", 2, 1, 3))

	reader := bufio.NewReader(os.Stdin)
	var problem Problem
	count := 0
	var testCase TestCase
	for {
		line, err := reader.ReadString('\n')
		if err == io.EOF {
			break
		}
		if problem.T == 0 {
			testCases, err := strconv.ParseInt(strings.TrimSuffix(line, string('\n')), 10, 64)
			if err != nil {
				break
			}
			problem.T = Int(testCases)
		} else {
			if count%2 == 0 {
				testCase = TestCase{}
				line = strings.TrimSuffix(line, string('\n'))
				inputValues := strings.Split(line, " ")

				testCase.dogFoodStock = getIntValue(inputValues[1])
				testCase.catFoodStock = getIntValue(inputValues[2])
				testCase.bonusCatFood = getIntValue(inputValues[3])

			} else {
				testCase.queue = strings.TrimSuffix(line, string('\n'))
				problem.testCases = append(problem.testCases, testCase)
			}

			count++

		}
	}

	PrintOutput(problem)

}
