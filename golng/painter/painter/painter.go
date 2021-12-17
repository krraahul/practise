package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"strconv"
	"sync"
)

type TestCase struct {
	size  int64
	panel []rune
}
type Problem struct {
	T         int64
	testCases []TestCase
}

var exist = struct{}{}
var colorMap map[rune]map[rune]struct{} = map[rune]map[rune]struct{}{
	'R': {
		'R': exist,
	},
	'Y': {
		'Y': exist,
	},
	'B': {
		'B': exist,
	},
	'O': {
		'R': exist,
		'Y': exist,
	},
	'P': {
		'R': exist,
		'B': exist,
	},
	'G': {
		'Y': exist,
		'B': exist,
	},
	'A': {
		'R': exist,
		'Y': exist,
		'B': exist,
	},
}

func calcMinCoat(currentColor rune, panel []map[rune]struct{}, ch chan int) {
	var lastPos int = -1
	sum := 0
	for index, currentGridColors := range panel {
		if _, bFound := currentGridColors[currentColor]; bFound {
			if lastPos == -1 {
				sum = 1
			} else if lastPos != index-1 {
				sum += 1
			}
			lastPos = index
		}
	}

	ch <- sum
}

func printAnswer(caseNumber int, input string) {
	//var input string = "YYGGBB"
	//var input string = "YYYBBBYYY"
	var panel []map[rune]struct{}

	for _, value := range input {

		c := colorMap[value]

		panel = append(panel, c)
		//fmt.Println(string(value))
	}
	var (
		ch           = make(chan int)
		finalSum int = 0
		mu       sync.Mutex
	)

	mu.Lock()
	defer mu.Unlock()
	go calcMinCoat('B', panel, ch)
	go calcMinCoat('R', panel, ch)
	go calcMinCoat('Y', panel, ch)

	for range []int{0, 1, 2} {
		res := <-ch

		finalSum += res
	}

	fmt.Printf("Case #%d: %d\n", caseNumber, finalSum)

}
func main() {
	scanner := bufio.NewReader(os.Stdin)

	problem := new(Problem)

	for {
		line, err := scanner.ReadBytes('\n')
		if err == io.EOF {
			break
		}
		if err != nil {
			return
		}
		//fmt.Println(" line = ", line)
		if problem.T == 0 {
			T, err := strconv.ParseInt(string(bytes.TrimSuffix(line, []byte("\n"))), 10, 32)
			if err != nil {
				break
			}
			problem.T = T
		} else {
			testCase := new(TestCase)
			s, err := strconv.ParseInt(string(bytes.TrimSuffix(line, []byte("\n"))), 10, 32)
			if err != nil {
				break
			}
			testCase.size = s
			line, err = scanner.ReadBytes('\n')
			if err != nil {
				break
			}
			testCase.panel = []rune(string(bytes.TrimSuffix(line, []byte("\n"))))

			tc := problem.testCases
			tc = append(tc, *testCase)
			problem.testCases = tc
		}

	}
	// fmt.Println(problem)
	for index, testCase := range problem.testCases {
		printAnswer(index+1, string(testCase.panel))
	}

	//fmt.Prinln(calcMinCoat() + calcMinCoat('Y', panel) + calcMinCoat('R', panel))
}
