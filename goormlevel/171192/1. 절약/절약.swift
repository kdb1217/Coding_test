let N = Int(readLine()!)!
var money: Int = 0
var flag: String = "success"
for _ in 0..<N {
	let tmp = readLine()!.split(separator: " ").map { String($0) }
	let command = tmp[0]
	let number = Int(tmp[1])!
	
	if command == "in" {
		money += number
	} else {
		money -= number
	}
	
	if money < 0 {
		flag = "fail"
		break
	}
}

print(flag)