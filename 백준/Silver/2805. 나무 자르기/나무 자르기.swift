import Foundation


let arr = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = arr[0]
let M = arr[1]

var trees = readLine()!.split(separator: " ").map { Int(String($0))! }
var start = 0
var last = trees.max()!
var result = 0

while start <= last {
    let mid = (start + last) / 2
    let tmp = trees.map { $0 - mid }.filter { $0 > 0 }.reduce(0, +)
    

    
    if tmp >= M {
        result = mid
        start = mid + 1
    } else {
        last = mid - 1
    }
}

print(result)
