import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    var answer = my_string.map{String($0)}[0..<s].joined() + overwrite_string
    answer += my_string.map{String($0)}[(s+overwrite_string.count)...].joined()
    return answer
}