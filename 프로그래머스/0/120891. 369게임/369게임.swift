import Foundation

func solution(_ order:Int) -> Int {
    var answer = 0
    let arr = String(order).map{$0}
    for i in arr {
        if i == "3" || i == "6" || i == "9" {
            answer += 1
        }
    }
    
    return answer
}