import Foundation

func solution(_ intStrs:[String], _ k:Int, _ s:Int, _ l:Int) -> [Int] {
    var answer: [Int] = []
    
    for i in intStrs {
        let tmp = Int(Array(i.map{String($0)}[s..<s + l]).joined())!
        if tmp > k {
            answer.append(tmp)
        }
    }
    return answer
}