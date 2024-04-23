import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    var tmp = myString.map{String($0)}
    var cnt = 0
    
    for i in 0..<(myString.count - pat.count + 1) {
        if Array(tmp[i..<i + pat.count]).joined() == pat {
            cnt += 1
        }
    }
    return cnt
}