let N = Int(readLine()!)!
var dScore: Int = 0
var pScore: Int = 0
for _ in 0..<N {
	let result = readLine()!
	
	if result == "D" {
		dScore += 1
	} else {
		pScore += 1
	}
	
	if abs(dScore - pScore) >= 2 {
		break
	}
}

print("\(dScore):\(pScore)")