import Foundation

func solution(_ num_list:[Int]) -> Int {
    var cnt = 0
    for i in num_list {
        var tmp = i
        while tmp != 1 {
            if tmp % 2 == 0 {
                tmp /= 2
                cnt += 1
            } else {
                tmp = (tmp - 1)/2
                cnt += 1
            }
        }
    }
    return cnt
}