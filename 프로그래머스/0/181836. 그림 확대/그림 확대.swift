import Foundation

func solution(_ picture:[String], _ k:Int) -> [String] {
    var answer: [String] = []
    for i in picture {
        var tmp = ""
        for j in i.map{String($0)} {
            let tmp2 = String(repeating: j, count: k)
            tmp += tmp2
        }
        for _ in 0..<k {
            answer.append(tmp)
        }
    }
    return answer
}