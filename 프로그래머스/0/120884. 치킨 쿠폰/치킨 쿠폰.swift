import Foundation

func solution(_ chicken:Int) -> Int {
    var cnt = 0
    var answer = 0
    if chicken == 0 {
        return 0
    }
    for i in 1...chicken {
        cnt += 1
        if cnt == 10 {
            answer += 1
            cnt = 1
        } 
    }
    return answer
}