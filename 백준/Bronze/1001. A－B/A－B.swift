import Foundation
let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let a = input.reduce(input[0] * 2) { $0 - $1}
print(a)

