import Foundation
import CoreFoundation
/*
풀이계획
1. 각 number에 맞는 배열의 배열에 
*/
func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var boards = board
    var answer: Int = 0
    var box: [Int] = []
    for i in moves {
        for j in 0..<board.count {
            if boards[j][i - 1] != 0 {
                box.append(boards[j][i - 1])
                boards[j][i - 1] = 0
                break
            }
        }
        
        if box.count >= 2 {
            if box[box.count-1] == box[box.count-2] {
                box.removeLast()
                box.removeLast()
                answer += 2
            }
        }
    }
    return answer
}
