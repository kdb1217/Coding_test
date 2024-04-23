import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = arr
    for i in queries {
        let start = i[0]
        let last = i[1]
        let standard = i[2]

        for j in start...last {
            if j % standard == 0 {
                answer[j] += 1
            }
        }
    }
    return answer
}