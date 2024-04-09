import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = []
    for i in 1...n {
        answer.append(i)
    }
    return answer.filter {$0 % 2 == 1}
}