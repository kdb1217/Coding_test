import Foundation
var input = readLine()!.split(separator: " ").map { String($0).replacingOccurrences(of: "1", with: "") }

var answer = "1"

print(answer+input.reduce("", +))
