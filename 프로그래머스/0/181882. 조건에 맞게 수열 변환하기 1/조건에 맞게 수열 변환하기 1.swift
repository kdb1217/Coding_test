import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer = arr
    for i in answer.indices {
        if answer[i] >= 50 && answer[i] % 2 == 0 {
            answer[i] /= 2
        } else if answer[i] < 50 && answer[i] % 2 == 1 {
            answer[i] *= 2
        }
    }
    return answer
}