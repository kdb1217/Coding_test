import Foundation

func solution(_ s:String) -> [Int] {
    let arr = s.map { String($0) }
    var dict: [String: Int] = [:]
    var answer: [Int] = []
    
    for i in 0..<arr.count {
        if dict[arr[i]] == nil {
            answer.append(-1)
            dict[arr[i]] = i
        } else {
            answer.append(i - dict[arr[i]]!)
            dict[arr[i]] = i
        }
    }
    return answer
}