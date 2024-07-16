import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dict: [String: Int] = [:]
    for i in 0..<clothes.count {
        dict[clothes[i][1],default: 0] += 1
    }
    var sum = 1
    for i in dict.values {
        sum *= (i + 1)
    }

    return sum - 1
}