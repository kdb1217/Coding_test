import Foundation

let input = Int(readLine()!)!
var range = 1...input
let str = "*"
for i in range {
    let repeatStar = String(repeating: str, count: i)
    print(repeatStar)
}
