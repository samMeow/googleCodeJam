package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func toIntArr(s string) []int {
	temp := strings.Split(strings.TrimSpace(s), " ")
	out := make([]int, len(temp))
	for i, v := range temp {
		value, _ := strconv.Atoi(v)
		out[i] = value
	}
	return out
}

func solution(data, pos []int) int {
	lookup := map[int][]int{}
	for i, v := range pos {
		if lookup[v-1] == nil {
			lookup[v-1] = []int{}
		}
		lookup[v-1] = append(lookup[v-1], i)
	}
	return 0
}

func main() {
	var buf string
	stdin := bufio.NewReader(os.Stdin)
	buf, _ = stdin.ReadString('\n')
	testcase, _ := strconv.Atoi(strings.TrimSpace(buf))
	for i := 0; i < testcase; i++ {
		stdin.ReadString('\n')
		line1, _ := stdin.ReadString('\n')
		line2, _ := stdin.ReadString('\n')
		result := solution(
			toIntArr(line1),
			toIntArr(line2),
		)
		fmt.Printf("Case: %d: %d\n", i+1, result)
	}
}
