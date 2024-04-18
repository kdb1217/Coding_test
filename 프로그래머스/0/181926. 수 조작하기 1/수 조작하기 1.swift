import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    var answer = n
    for i in control {
        if i == "w" {
            answer += 1
        } else if i == "s" {
            answer -= 1
        } else if i == "d" {
            answer += 10
        } else if i == "a" {
            answer -= 10
        }
    }
    return answer
}