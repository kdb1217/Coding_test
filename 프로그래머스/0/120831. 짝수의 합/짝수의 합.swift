import Foundation

func solution(_ n:Int) -> Int {
    var answer: Int = 0
    for i in 1...n {
        if i % 2 == 0 {
            answer += i
        }
    }
    return answer
}