import Foundation

func solution(_ i:Int, _ j:Int, _ k:Int) -> Int {
    var answer: [Int] = []
    var cnt = 0
    for i in stride(from: i, through:j, by: 1) {
        answer.append(i)
    }
    var tmp = answer.map{String($0)}
    for i in tmp {
        cnt += i.map{String($0)}.filter{$0 == String(k)}.count 
    }
    return cnt
}