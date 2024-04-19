import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer = strArr
    for i in strArr.indices {
        if i % 2 == 0 {
            answer[i] = String(strArr[i].lowercased())
        } else if i % 2 == 1 {
            answer[i] = String(strArr[i].uppercased())
        }
    }
    return answer
}