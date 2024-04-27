import Foundation

func solution(_ strArr:[String]) -> Int {
    var arr = strArr.map{$0.count}
    var answer: [Int] = []
    for i in 1...arr.max()! {
        answer.append(strArr.filter{$0.count == i}.count)
    }
    
    
    return answer.max()!
}