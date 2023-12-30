import Foundation

var a: [Int] = []
for _ in 0...8 {
    var input = Int(readLine()!)!
    a.append(input)
}
let maxnum: Int = a.max() ?? 0
let maxidx: Int = a.firstIndex(of: maxnum ) ?? 0

print(maxnum)
print(maxidx + 1)
