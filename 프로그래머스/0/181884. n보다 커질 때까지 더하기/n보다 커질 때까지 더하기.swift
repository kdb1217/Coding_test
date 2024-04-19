import Foundation

func solution(_ numbers:[Int], _ n:Int) -> Int {
    var answer: Int = 0
    
    for i in numbers {
        if answer > n {
            break
        }
        answer += i
    }
    
    return answer
}