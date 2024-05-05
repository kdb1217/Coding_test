import Foundation

func solution(_ l:Int, _ r:Int) -> [Int] {
    var answer: [Int] = []
    for i in l...r {
        var tmp = Set(String(i).map {Int(String($0))!})
        if tmp == [0,5] || tmp == [0] || tmp == [5] {
            answer.append(i)
        }
    }
    return answer.isEmpty ? [-1] : answer
}