let arr = readLine()!.split(separator: " ").map { Int($0)! }
let N = arr[0]
let C = arr[1]
let times = readLine()!.split(separator: " ").map { Int($0)! }
var textCount: Int = 0

for i in 0..<times.count-1 {
	if times[i + 1] - times[i] > C {
		textCount = 0
	} else {
		textCount += 1
	}
}

print(textCount+1)