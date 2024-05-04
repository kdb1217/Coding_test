import Foundation

func solution(_ my_string:String) -> Int {
    let arr = my_string.split(separator: " ").map {String($0)}
    var answer = 0
    for i in 0..<arr.count {
        if arr[i] == "+" {
            if i == 1 {
                answer = Int(arr[i - 1])! + Int(arr[i + 1])!
            } else {
                answer += Int(arr[i + 1])!
            }
        } else if arr[i] == "-" {
            if i == 1 {
                answer = Int(arr[i - 1])! - Int(arr[i + 1])!
            } else {
                answer -= Int(arr[i + 1])!
            }
        }
    }
    return answer
}