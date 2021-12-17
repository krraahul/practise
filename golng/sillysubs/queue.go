package main

type any interface{}

type QueueInterface interface {
	Push(item any) any
	Pop() any
	IsEmpty() bool
	Top() any
}
type Queue struct {
	arr []any
}

func (Q *Queue) New() Queue {
	return Queue{
		arr: []any{},
	}
}

func (Q *Queue) Push(item any) any {
	Q.arr = append(Q.arr, item)
	return item
}

func (Q *Queue) Pop() any {
	if Q.IsEmpty() {
		return nil
	} else {
		res := Q.arr[0]
		Q.arr = Q.arr[1:]
		return res
	}
}

func (Q *Queue) IsEmpty() bool {
	return len(Q.arr) == 0
}
