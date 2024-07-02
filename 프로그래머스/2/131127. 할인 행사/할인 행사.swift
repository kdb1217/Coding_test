import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    var dict: [String: Int] = [:]
    var tmpDict: [String: Int] = [:]
    var cnt: Int = 0
    
    for i in 0..<number.count {
        dict[want[i]] = number[i]
    }
    for i in 0...(discount.count - number.reduce(0, +)) {
        var tmpDict: [String: Int] = [:]
        for j in i..<(i + number.reduce(0, +)) {
            tmpDict[discount[j], default: 0] += 1
        }
        if tmpDict == dict {
            cnt += 1
        }
    }
    return cnt
}