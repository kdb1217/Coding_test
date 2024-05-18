func solution(_ s:String) -> Int {
    var answer = s.map {String($0)}
    return answer[0] == "-" ? Int(answer.joined())! : Int(answer.joined())!
}