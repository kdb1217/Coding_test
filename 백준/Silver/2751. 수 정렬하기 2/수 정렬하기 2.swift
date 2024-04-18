import Foundation

let num = Int(readLine()!)!
var arr: [Int] = []
for i in 1...num {
    arr.append(Int(readLine()!)!)
}
let answer = arr.sorted()

for i in answer {
    print(i)
}
