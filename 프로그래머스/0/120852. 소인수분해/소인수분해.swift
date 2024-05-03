import Foundation

func solution(_ n:Int) -> [Int] {
    var num = n
    var answer: Set<Int> = []
    var cnt = 2
    
    while num != 1 {
        if num % cnt == 0 {
            num /= cnt
            answer.update(with: cnt)
            cnt = 2
        } else {
            cnt += 1
        }
    }
    return Array(answer).sorted()
}