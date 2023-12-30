import Foundation

let input = readLine()!
let inputNum = Int(readLine()!)!
var answer = input[input.index(input.startIndex, offsetBy: inputNum - 1)]

print(answer)
