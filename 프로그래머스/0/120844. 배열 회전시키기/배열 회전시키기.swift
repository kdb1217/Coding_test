import Foundation

func solution(_ numbers:[Int], _ direction:String) -> [Int] {
    if direction == "right" {
        return Array(Array(numbers[numbers.count-1...numbers.count-1]) + Array(numbers[0...numbers.count-2]))
    } else {
        return Array(Array(numbers[1...]) + Array(numbers[0...0]))
    }
}