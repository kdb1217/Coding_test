import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    var answer = (array + [n]).sorted()
 
    if answer.last! == n {
        return answer[answer.firstIndex(of: n)! - 1]
    } else if answer.first! == n {
        return answer[answer.firstIndex(of: n)! + 1]
    } else {
        var small = abs(answer[answer.firstIndex(of: n)! - 1] - n)
        var big = abs(answer[answer.firstIndex(of: n)! + 1] - n)
        if small == big {
            return answer[answer.firstIndex(of: n)! - 1]          
        } else {
            return small > big ? answer[answer.firstIndex(of: n)! + 1] : answer[answer.firstIndex(of: n)! - 1]
        }
    }
}