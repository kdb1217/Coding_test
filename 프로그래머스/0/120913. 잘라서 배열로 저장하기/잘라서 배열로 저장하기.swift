import Foundation

func solution(_ my_str:String, _ n:Int) -> [String] {
    var answer: [String] = []
    var arr = my_str.map{String($0)}
    var tmp = ""
    for i in 0..<arr.count {
        tmp += arr[i]
        if tmp.count == n {
            answer.append(tmp)
            tmp = ""
        }
    }
    if tmp != "" {
        answer.append(tmp)
    }
    return answer
}