import Foundation

func solution(_ babbling:[String]) -> Int {
    var answer = 0
    let able:[String] = ["aya","ye","woo","ma"]
    for i in babbling {
        var tmp: String = i
        for j in able {
            tmp = tmp.replacingOccurrences(of: j, with:" ")
        }
        if tmp.replacingOccurrences(of: " ", with: "") == "" {
            answer += 1
        }

    }
    return answer
}