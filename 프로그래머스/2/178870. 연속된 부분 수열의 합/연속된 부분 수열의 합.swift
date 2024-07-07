import Foundation

func solution(_ sequence:[Int], _ k:Int) -> [Int] {
    var start = 0
    var end = 0
    var answer: [[Int]] = []
    var sum = sequence[0]
    
    while start < sequence.count && end < sequence.count {
        if sum <= k {
            if sum == k {
                answer.append([start, end])
            }
            end += 1
            if end == sequence.count { break }
            sum += sequence[end]
        } else {
            if start == sequence.count { break }
            sum -= sequence[start]
            start += 1
        }
    }
    answer = answer.sorted { $0[1] - $0[0] == $1[1] - $1[0] ? $0[0] < $1[0] : ($0[1] - $0[0] < $1[1] - $1[0])}
    return answer.isEmpty ? [0] : answer.first!
}