import Foundation

func solution(_ s:String) -> Int{
    let arr = s.map { String($0) }
    var answer: [String] = []
    
    for i in arr {
        answer.append(i)
        if answer.count >= 2 {
            if answer.last! == answer[answer.count-2] {          
                answer.removeLast()
                answer.removeLast()
            }
        }
    }
    return answer.isEmpty ? 1 : 0
}