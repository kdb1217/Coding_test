import Foundation

func solution(_ quiz:[String]) -> [String] {
    var answer: [String] = []
    for i in quiz {
        let tmp = i.split(separator: " ").map{String($0)}
        if tmp[1] == "-" {
            if Int(tmp[0])! - Int(tmp[2])! == Int(tmp[4])! {
                answer.append("O")
            } else {
                answer.append("X")
            }
        } else {
            if Int(tmp[0])! + Int(tmp[2])! == Int(tmp[4])! {
                answer.append("O")
            } else {
                answer.append("X")
            }
        }
    }
    return answer
}