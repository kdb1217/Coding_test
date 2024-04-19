import Foundation

func solution(_ myString:String) -> String {
    var answer = myString.map{($0)}
    for i in answer.indices {
        if answer[i].asciiValue! < Character("l").asciiValue! {
            answer[i] = "l"
        }
    }
    return answer.map{String($0)}.joined()
}