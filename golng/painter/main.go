package main

import (
	"bufio"
	painter "mymodules/painter/painter"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewReader(os.Stdin)
	// if err := scanner.Err(); err != nil {
	// 	fmt.Println("Error")
	// }

	problem := new(painter.Problem)

	// for scanner.Scan() {
	// 	line := scanner.Text()
	// 	//fmt.Println(" line = ", line)
	// 	if problem.T == 0 {
	// 		T, err := strconv.ParseInt(line, 10, 32)
	// 		if err != nil {
	// 			break
	// 		}
	// 		problem.T = T
	// 	} else {
	// 		testCase := new(painter.TestCase)
	// 		s, err := strconv.ParseInt(line, 10, 32)
	// 		if err != nil {
	// 			break
	// 		}
	// 		testCase.Size = s
	// 		scanner.Scan()
	// 		testCase.Panel = []rune(scanner.Text())

	// 		tc := problem.TestCases
	// 		tc = append(tc, *testCase)
	// 		problem.TestCases = tc
	// 	}

	// }
	for {
		line, err := scanner.ReadBytes('\n')
		if err != nil {
			return
		}
		//fmt.Println(" line = ", line)
		if problem.T == 0 {
			T, err := strconv.ParseInt(string(line), 10, 32)
			if err != nil {
				break
			}
			problem.T = T
		} else {
			testCase := new(painter.TestCase)
			s, err := strconv.ParseInt(string(line), 10, 32)
			if err != nil {
				break
			}
			testCase.Size = s
			line, err = scanner.ReadBytes('\n')
			if err != nil {
				return
			}
			testCase.Panel = []rune(string(line))

			tc := problem.TestCases
			tc = append(tc, *testCase)
			problem.TestCases = tc
		}

	}
	for index, testCase := range problem.TestCases {
		painter.PrintAnswer(index+1, string(testCase.Panel))
	}

	//fmt.Prinln(calcMinCoat() + calcMinCoat('Y', panel) + calcMinCoat('R', panel))
}
