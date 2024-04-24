import Foundation

func solution(_ q:Int, _ r:Int, _ code:String) -> String {
    var answer = ""
    var arr = code.map{ String($0) }
    
    for i in 0..<arr.count {
        if i % q == r {
            answer = answer + arr[i]
        }
    }
    return answer
}