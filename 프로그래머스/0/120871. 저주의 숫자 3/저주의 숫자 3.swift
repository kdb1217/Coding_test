import Foundation

func solution(_ n:Int) -> Int {
    var answer = 0
    for _ in 1...n {
        answer += 1
        while answer % 3 == 0 || String(answer).contains("3") {
            answer += 1
        }
    }
    return answer
}