import Foundation


let firstInput = readLine()!.split(separator: " ").map { Int(String($0))! }

let inputNum = readLine()!.split(separator: " ").map { Int(String($0))! }

var answer: [Int] = []
for i in 0...inputNum.count - 1 {
    if inputNum[i] < firstInput[1] {
        answer.append(inputNum[i])
    }
}
let result = answer.map { String($0) }.joined(separator: " ")
print(result)
