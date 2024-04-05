import Foundation

func solution(_ num1:Int, _ num2:Int) -> Int {
    var num: Double = Double(num1) / Double(num2)
    num *= 1000
    return Int(num)
}