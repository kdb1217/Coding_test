import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    var answer = ""
    var arr = my_string.map{$0}
    for i in stride(from: c - 1, to: my_string.count, by: m) {
        answer += String(arr[i])
    }
    return answer
}