import Foundation

let num = Int(readLine()!)!
var answer: [Int] = []
for _ in 1...num {
    let tmp = Int(readLine()!)!
    if tmp == 0 {
        answer.removeLast()
    } else {
        answer.append(tmp)
    }
}

print(answer.reduce(0, +))
