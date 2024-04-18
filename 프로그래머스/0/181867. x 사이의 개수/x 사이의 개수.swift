import Foundation

func solution(_ myString:String) -> [Int] {
    var cnt: Int = 0
    var answer: [Int] = []
    for i in myString {
        if i == "x" {
            answer.append(cnt)
            cnt = 0
        } else {
            cnt += 1
        }
    }
    answer.append(cnt)

    return answer
}