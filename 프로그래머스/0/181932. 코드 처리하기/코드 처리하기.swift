import Foundation

func solution(_ code:String) -> String {
    var mode: Int = 0
    var arr: [String] = code.map{String($0)}
    var answer: String = ""
    for i in 0..<arr.count {
        if i % 2 == 0 && arr[i] != "1" && mode == 0{
            answer += arr[i]
        } else if arr[i] == "1" && mode == 0 {
            mode = 1
        } else if arr[i] != "1" && i % 2 == 1 && mode == 1 {
            answer += arr[i]
        } else if arr[i] == "1" && mode == 1 {
            mode = 0
        }
    }
    return answer.isEmpty ? "EMPTY" : answer
}