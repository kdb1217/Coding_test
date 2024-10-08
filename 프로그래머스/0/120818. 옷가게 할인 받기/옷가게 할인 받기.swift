import Foundation

func solution(_ price:Int) -> Int {
    var answer = price
    if price >= 500000 {
        answer = Int(floor(Double(price) * 0.8))
    } else if price >= 300000 {
        answer = Int(floor(Double(price) * 0.9))
    } else if price >= 100000 {
        answer = Int(floor(Double(price) * 0.95))
    }
    return answer
}