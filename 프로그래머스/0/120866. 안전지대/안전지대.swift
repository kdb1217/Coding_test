import Foundation

func solution(_ board:[[Int]]) -> Int {
    var arr = board
    return arr.flatMap {$0}.filter {$0 == 0}.count
}