import Foundation
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let N = arr[0]
let M = arr[1]

let salt: Double = 7 * Double(N) / 100

var answer: Double = salt / Double(N + M) * 100 
answer = floor(answer * 100) / 100
print(String(format: "%.2f", answer))