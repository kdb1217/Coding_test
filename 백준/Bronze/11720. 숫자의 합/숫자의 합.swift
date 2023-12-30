import Foundation

let n = Int(readLine()!)!

let input = Array(readLine()!)
let result = input.map { Int(String($0))!}

let answer = result.reduce(0) {$0 + $1}

print(answer)
