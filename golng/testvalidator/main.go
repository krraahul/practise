package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path"

	painter "mymodules/painter/painter"
)

func main() {
	baseDir, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}
	sPath := path.Clean("./painter/painter/test_data/test_set_1/ts1_input.txt")
	sPath = path.Join(baseDir, sPath)
	fmt.Println(sPath)
	file, err := os.OpenFile(sPath, os.O_RDONLY, os.ModeAppend)
	if err != nil {
		fmt.Println(" I am here", err)
		log.Fatal("Fatal error in opening file")

	}
	inputReader := bufio.NewReader(file)
	count := 0
	for {
		line, err := inputReader.ReadBytes('\n')
		if err != nil {
			log.Fatal(err)
			break
		}
		st := string(line)
		fmt.Println("size of line ", count, " is ", len(st))
		count++
	}
	fmt.Println("Number of lines = ", count)
	fmt.Println(new(painter.Problem).T)
	fmt.Println("second project")
}
