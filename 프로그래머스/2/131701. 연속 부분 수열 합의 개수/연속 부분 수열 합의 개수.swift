import Foundation

func solution(_ elements:[Int]) -> Int {
    var numsSet: Set<Int> = []
    let numbers = elements + elements 
    var tmp = 0
 
    for i in 0..<elements.count {
        tmp = 0
        for j in i..<i + elements.count {
            tmp += numbers[j]
            numsSet.insert(tmp)
        }
    }
    
    return numsSet.count
}