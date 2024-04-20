import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer = arr 
    for i in queries {
        for j in i[0]...i[1] {
            answer[j] = answer[j] + 1
        }
    }
    return answer
}