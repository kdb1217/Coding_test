let N = Int(readLine()!)!

for i in 1...N * N {
	if i % N != 0 {
		print(i, terminator: " ")
	}
	else {
		print(i)
	}
}