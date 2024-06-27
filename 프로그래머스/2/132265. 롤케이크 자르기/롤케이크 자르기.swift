import Foundation

func solution(_ topping:[Int]) -> Int {
    var count = 0
    var brotherDict: [Int:Int] = [:]
    var myDict: [Int: Int] = [:]
    for i in 0..<topping.count {
        brotherDict[topping[i], default: 0] += 1
    }
    
    for i in 0..<topping.count {
        brotherDict[topping[i]]! -= 1
        
        if brotherDict[topping[i]]! == 0 {
            brotherDict[topping[i]] = nil
        }
        
        myDict[topping[i], default: 0] += 1
        
        if brotherDict.keys.count == myDict.keys.count {
            count += 1
        }
    }
    
    return count
}