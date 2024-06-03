import Foundation


func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for i in commands {
        let tmp = Array(array[i[0]-1...i[1]-1]).sorted()
        let num = i[2] - 1
        answer.append(tmp[num])
    }
    return answer
}