import Foundation

func solution(_ score:[[Int]]) -> [Int] {
    var array: [Int] = []
    var answer: [Int] = []
    for i in score {
        array.append(i.reduce(0, +) / 2)
    }
    var tmp = Array(Set(array)).sorted(by: >)
    var d = 0
    for i in array {
        if array.filter{$0 == i}.count > 1 {
            d +=  array.filter{$0 == i}.count - 1
        }
        answer.append(tmp.firstIndex(of: i)! + d)
    }
    return answer
}