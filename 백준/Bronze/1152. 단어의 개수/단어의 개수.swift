import Foundation

let input = readLine()!

var result = input.components(separatedBy: " ")
while (result.contains("")) {
    if let idx = result.lastIndex(of: "") {
        result.remove(at: idx)
    }
}
print(result.count)
