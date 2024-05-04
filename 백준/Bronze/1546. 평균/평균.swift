import Foundation

let n = Int(readLine()!)!
var scores = readLine()!.split(separator: " ").map {Double($0)!}
scores.sort()
var maxScore = scores.last!

scores = scores.map {Double($0/maxScore*100)}

print(scores.reduce(0.0, +) / Double(scores.count))
