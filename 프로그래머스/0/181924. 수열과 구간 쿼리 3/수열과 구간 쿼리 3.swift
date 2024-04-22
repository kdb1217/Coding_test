import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer = arr
    for i in queries {
        answer.swapAt(i[0], i[1])
    }
    return answer
}