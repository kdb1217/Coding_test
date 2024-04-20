import Foundation

func solution(_ str1:String, _ str2:String) -> String {
    var arr1 = str1.map{String($0)}
    var arr2 = str2.map{String($0)}
    var answer = ""
    for i in 0..<arr1.count {
        answer += arr1[i]
        answer += arr2[i]
    }
    return answer
}