import Foundation

func solution(_ arr:[Int], _ intervals:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for i in 0..<intervals.count {
        answer.append(contentsOf: arr[intervals[i][0]...intervals[i][1]])
    }
    return answer
}