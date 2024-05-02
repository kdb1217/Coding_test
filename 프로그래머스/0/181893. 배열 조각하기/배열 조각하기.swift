import Foundation

func solution(_ arr:[Int], _ query:[Int]) -> [Int] {
    var answer = arr
    for i in 0..<query.count {
        if i % 2 == 0 {
            answer = Array(answer[0...query[i]])
        } else {
            answer = Array(answer[query[i]...])
        }
    }
    return answer
}