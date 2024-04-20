import Foundation

func solution(_ s:String) -> String {
    var answer = ""
    for i in s {
        if s.map{$0}.filter{$0 == i}.count == 1 {
            answer += String(i)
        }
    }
    return answer.map{String($0)}.sorted().joined()
}