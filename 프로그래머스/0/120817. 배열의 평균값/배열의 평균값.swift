import Foundation

func solution(_ numbers:[Int]) -> Double {
    var total: Int = numbers.reduce(0) {return $0 + $1} 
    return Double(total) / Double(numbers.count) 
}