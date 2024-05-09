import Foundation

func solution(_ score:[[Int]]) -> [Int] {
    var array: [Double] = []
    var answer: [Int] = []
    for i in score {
        array.append(Double(i.reduce(0, +)) / Double(2))
    }
    var tmp = array.sorted(by: >)
    for i in array {
        answer.append(tmp.firstIndex(of: i)! + 1)
    }
    return answer
}