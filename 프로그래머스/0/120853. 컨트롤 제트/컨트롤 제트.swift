import Foundation

func solution(_ s:String) -> Int {
    var arr = s.split(separator:" ")
    var answer = 0
    for i in 0..<arr.count {
        if arr[i] == "Z" {
            answer -= Int(arr[i - 1])!
        }
        else {
            answer += Int(arr[i])!
        }
    }
    return answer
}