import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for i in queries {
        var tmp: [Int] = []
        for j in stride(from:i[0], through:i[1], by:1) {
            if arr[j] > i[2] {
                tmp.append(arr[j])
            }
        }
        answer.append(tmp.min() ?? -1)
    }
    return answer
}