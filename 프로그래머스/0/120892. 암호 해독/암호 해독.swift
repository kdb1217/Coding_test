import Foundation

func solution(_ cipher:String, _ code:Int) -> String {
    let arr = cipher.map {String($0)}
    var answer = ""
    for (index, result) in arr.enumerated() {
        if (index + 1) % code == 0 {
            answer += result
        }
    }
    return answer
}