import Foundation

func solution(_ arr:[Int], _ flag:[Bool]) -> [Int] {
    var answer: [Int] = []
    for i in flag.indices {
        if flag[i] == true {
            let tmp = Array(repeating: arr[i], count: (arr[i] * 2))
            answer.append(contentsOf: tmp)
        } else {
            answer.removeLast(arr[i])
        }
    }
    return answer
}