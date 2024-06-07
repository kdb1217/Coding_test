import Foundation

/* 풀이계획
*/
func solution(_ s:String) -> Int {
    var answer: Int = 0
    var firstCount: Int = 0
    var secondCount: Int = 0
    var firstChar: String = ""
    var arr = s.map { String($0) }
    
    for i in arr {
        if firstCount == 0 && secondCount == 0 {
            firstChar = i
        }
        
        if firstChar == i {
            firstCount += 1
        } else {
            secondCount += 1   
        }
        
        if firstCount == secondCount && secondCount != 0 {
            answer += 1
            firstChar = ""
            firstCount = 0
            secondCount = 0
        }
    }
    if firstCount != 0 {
        answer += 1
    }
    
    return answer
}