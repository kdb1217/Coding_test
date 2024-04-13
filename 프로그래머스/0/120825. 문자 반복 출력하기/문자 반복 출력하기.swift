import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    var arr = my_string.map {$0}
    var answer = ""
    for i in arr {
        answer += String(repeating: i, count: n)
    }
    return answer
}