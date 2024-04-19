import Foundation

func solution(_ my_string:String) -> [String] {
    var answer: [String] = []
    for i in stride (from:my_string.count, to: 0 , by: -1) {
        answer.append(String(my_string.suffix(i)))
    }
    return answer.sorted()
}