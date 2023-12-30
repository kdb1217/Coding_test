import Foundation

let n = Int(readLine()!)!

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let max = input.max() ?? 0
let min = input.min() ?? 0
print("\(min) \(max)")
