import Foundation

func solution(_ arr:[Int], _ k:Int) -> [Int] {
    var answer: [Int] = []
    for i in arr {
        if !answer.contains(i) {
            answer.append(i)
        }
        if answer.count == k {
            break
        }
    }
    if k > answer.count {
        for i in 0..<k-answer.count {
            answer.append(-1)
        }
    } else {
        return Array(answer[0..<k])
    }
    return answer
}