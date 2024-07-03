import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int {
    var user1 = a
    var user2 = b
    var answer = 1
    
    while true {
        if abs(user1 - user2) == 1 && max(user1, user2) % 2 == 0 {
            break
        } else {
            answer += 1
        }
        user1 = (user1 + 1) / 2
        user2 = (user2 + 1) / 2
    } 
    return answer
}