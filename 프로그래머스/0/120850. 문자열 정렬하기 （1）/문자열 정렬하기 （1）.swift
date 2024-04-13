import Foundation

func solution(_ my_string:String) -> [Int] {
    var arr = Array(my_string)
    var answer: [Int] = []
    for i in arr {
        if i.isNumber {
            answer.append(Int((String(i)))!)
        }
    }
    return answer.sorted()
}