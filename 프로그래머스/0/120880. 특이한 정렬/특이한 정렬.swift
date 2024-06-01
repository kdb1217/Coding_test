import Foundation

func solution(_ numlist:[Int], _ n:Int) -> [Int] {
    var answer = numlist.sorted {
        let diff1 = abs(n - $0)
        let diff2 = abs(n - $1)
        
        if diff1 == diff2 {
            return $0 > $1
        } else {
            return diff1 < diff2
        }
    }
    return answer
}