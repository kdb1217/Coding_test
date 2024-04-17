import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer: [Int] = []
    for i in arr {
        for j in stride(from:0, to: i, by: 1) {
            answer.append(i)
        }
    }
    return answer
}