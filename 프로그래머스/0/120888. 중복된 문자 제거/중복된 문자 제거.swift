import Foundation

func solution(_ my_string:String) -> String {
    var answer = ""
    for i in my_string {
        if answer.map{$0}.filter{$0 == i}.count == 0 {
            answer += String(i)
        }
    }
    return answer
}