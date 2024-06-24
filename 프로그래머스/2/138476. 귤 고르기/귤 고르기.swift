import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var dict: [Int:Int] = [:]
    var tmp = k
    var cnt = 0
    
    for i in tangerine {
        dict[i,default: 0] += 1
    }
    var arr = dict.keys.sorted { dict[$0]! > dict[$1]! }
    
    for i in arr {
        tmp -= dict[i]!
        cnt += 1
        if tmp <= 0 {
            break
        }
    }
    return cnt
}