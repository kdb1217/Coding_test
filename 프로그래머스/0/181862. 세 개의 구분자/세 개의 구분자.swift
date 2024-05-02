import Foundation

func solution(_ myStr:String) -> [String] {
    var answer = myStr.components(separatedBy: ["a","b","c"])
    answer = answer.filter {$0.count != 0}
    return answer.isEmpty ? ["EMPTY"] : answer
}