import Foundation

func solution(_ lines:[[Int]]) -> Int {
    var answer = Array(repeating: 0, count:201)
    
    for i in lines {
        for j in i[0] + 100 ..< i[1] + 100 {
            answer[j] += 1
        }
    }
    return answer.filter{$0 > 1}.count
}