import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    var answer = myString.map {String($0 == "A" ? "B" : "A")}
    return answer.joined().contains(pat) ? 1 : 0
}