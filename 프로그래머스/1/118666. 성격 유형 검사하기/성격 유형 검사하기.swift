import Foundation

/*
풀이계획
1. 각각의 유형마다 딕셔너리로 초기화 한다.
*/
func solution(_ survey:[String], _ choices:[Int]) -> String {
    var result: [String : Int] = ["R": 0,"T": 0,"C": 0, "F" : 0, "J": 0, "M": 0, "A": 0, "N": 0]
    var answer = ""
    for i in 0..<survey.count {
        let postive = String(survey[i].first!)
        let negative = String(survey[i].last!)
        if choices[i] > 4 {
            result[negative, default: 0] += choices[i] % 4
        } else if choices[i] < 4 {
            result[postive, default: 0] += abs(choices[i] - 4)
        }
    }
    answer += result["R"]! >= result["T"]! ? "R" : "T"
    answer += result["C"]! >= result["F"]! ? "C" : "F"
    answer += result["J"]! >= result["M"]! ? "J" : "M"
    answer += result["A"]! >= result["N"]! ? "A" : "N"
    return answer
}