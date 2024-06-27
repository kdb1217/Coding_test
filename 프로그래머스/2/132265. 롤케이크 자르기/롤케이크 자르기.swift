import Foundation

func solution(_ topping:[Int]) -> Int {
    var count = 0
    
    for i in 0..<topping.count - 1 {
        if Set(Array(topping[0...i])).count == Set(Array(topping[(i+1)...])).count {
            count += 1
        } 
    }
    return count
}