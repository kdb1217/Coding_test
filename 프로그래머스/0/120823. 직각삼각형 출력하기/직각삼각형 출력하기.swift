import Foundation

let n = Int(readLine()!)!

for i in stride(from: 1, through: n, by: 1) {
    let tmp = String(repeating: "*", count: i)
    print(tmp)
}