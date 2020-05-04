package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func readData(reader *bufio.Reader) []uint64 {
	temp, _ := reader.ReadString('\n')
	ar := strings.Split(strings.TrimRight(temp, "\n"), " ")
	total, _ := strconv.Atoi(ar[1])

	out := make([]uint64, total)
	temp, _ = reader.ReadString('\n')
	ar = strings.Split(strings.TrimRight(temp, "\n"), " ")
	for idx, el := range ar {
		out[idx], _ = strconv.ParseUint(el, 10, 64)
	}

	return out
}

func gcd(A, B uint64) uint64 {
	x := A
	y := B
	if y > x {
		x = B
		y = A
	}
	for ok := true; ok; ok = (y != 0) {
		x, y = y, uint64(math.Mod(float64(x), float64(y)))
	}
	return x
}

func uniq(seq []uint64) []uint64 {
	occr := map[uint64]bool{}
	out := []uint64{}
	for _, el := range seq {
		if occr[el] {
			continue
		}
		occr[el] = true
		out = append(out, el)
	}
	return out
}

func sort(seq []uint64) []uint64 {
	for i := 0; i < len(seq); i++ {
		for j := 0; j < len(seq)-1; j++ {
			if seq[j] > seq[j+1] {
				temp := seq[j+1]
				seq[j+1] = seq[j]
				seq[j] = temp
			}
		}
	}
	return seq
}

func asDict(seq []uint64) map[uint64]byte {
	uppercase := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	out := map[uint64]byte{}
	for idx, el := range seq {
		out[el] = uppercase[idx]
	}
	return out
}

func solve(seq []uint64) string {
	out := make([]uint64, len(seq)+1)
	out[1] = gcd(seq[0], seq[1])
	out[0] = uint64(seq[0] / out[1])
	for idx, el := range seq {
		out[idx+1] = uint64(el / out[idx])
	}

	used := sort(uniq(out))
	lookup := asDict(used)
	str := []byte{}
	for _, el := range out {
		str = append(str, lookup[el])
	}

	return string(str)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	temp, _ := reader.ReadString('\n')
	times, _ := strconv.Atoi(strings.TrimRight(temp, "\n"))
	fmt.Println()

	for i := 0; i < times; i++ {
		data := readData(reader)
		str := solve(data)
		fmt.Printf("Case #%d: %s\n", i+1, str)
	}
}
