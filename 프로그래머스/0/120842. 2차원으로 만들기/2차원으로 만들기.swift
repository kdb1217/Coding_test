import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [[Int]] {
    var answer: [[Int]] = []
    var tmp: [Int] = []
    for i in 0..<num_list.count {
        tmp.append(num_list[i])
        if tmp.count == n {
            answer.append(tmp)
            tmp = []
        }
    }
    return answer
}