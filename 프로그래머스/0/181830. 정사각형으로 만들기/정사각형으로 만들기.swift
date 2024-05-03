import Foundation

func solution(_ arr:[[Int]]) -> [[Int]] {
    let diff = arr.count - arr[0].count
    var answer = arr
    if diff > 0 {
        for i in 0..<arr.count {
            for _ in 0..<diff {
                answer[i].append(0)
            }
        }
    } else if diff < 0 {
        for i in 0..<abs(diff) {
            answer.append(Array(repeating: 0, count: arr[0].count))
        }
    } else {
        return answer
    }
    
    return answer
}