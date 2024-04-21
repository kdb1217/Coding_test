import Foundation

func solution(_ keyinput:[String], _ board:[Int]) -> [Int] {
    var answer = [0,0]
    for i in keyinput {
        switch i {
            case "up":
                if board[1] / 2 > answer[1] {
                    answer[1] += 1
                }
            case "down":
                if -(board[1] / 2) < answer[1] {
                    answer[1] -= 1
                }
            case "left":
                if -(board[0] / 2) < answer[0] {
                    answer[0] -= 1
                }
            default:
                if board[0] / 2 > answer[0] {
                    answer[0] += 1
                }
                
        }
    }
    return answer
}