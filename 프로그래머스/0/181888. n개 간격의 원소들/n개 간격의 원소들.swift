import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var answer: [Int] = []
    for i in stride(from: 0, through: num_list.count-1, by: n) {
        answer.append(num_list[i])
    }
    return answer
}