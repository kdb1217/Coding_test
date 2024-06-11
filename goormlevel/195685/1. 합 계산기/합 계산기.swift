let n = Int(readLine()!)!
var total: Int = 0

for _ in 0..<n {
	let tmp = readLine()!.split(separator: " ").map { String($0) }
	let num1 = Int(tmp[0])!
	let sign = tmp[1]
	let num2 = Int(tmp[2])!
	
	if sign == "+" {
		total += num1 + num2
	} else if sign == "-" {
		total += (num1 - num2)
		
	} else if sign == "*" {
		total += num1 * num2
		
	} else {
		total += num1 / num2 
	}
}

print(total)