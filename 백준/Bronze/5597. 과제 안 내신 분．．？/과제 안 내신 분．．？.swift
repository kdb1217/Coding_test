import Foundation

let studentNumbers: Set<Int> = Set(1...30)
var currentNum: Set<Int> = []
for _ in 1...28 {
    let num = Int(readLine()!)!
    currentNum.insert(num)
}

var answer = studentNumbers.subtracting(currentNum)
var answerArr = Array(answer)
answerArr.sort()
answerArr.forEach {
    print($0)
}
