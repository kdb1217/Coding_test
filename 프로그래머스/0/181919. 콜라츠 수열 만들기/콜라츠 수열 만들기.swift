import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = [n]
    var a = n
    while a != 1 {
        if a % 2 == 0 {
            a /= 2
            answer.append(a)
        } else {
            a = a * 3 + 1
            answer.append(a)
        }
    }
    return answer
}