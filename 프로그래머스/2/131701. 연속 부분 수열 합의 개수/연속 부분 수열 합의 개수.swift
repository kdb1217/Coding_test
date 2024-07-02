import Foundation

func solution(_ elements:[Int]) -> Int {
    var numsSet: Set<Int> = []
    let numbers = elements + elements 
    
 
    for i in 0..<elements.count {
        for j in i..<i + elements.count {
            numsSet.insert(Array(numbers[i...j]).reduce(0, +))
        }
    }
    
    return numsSet.count
}