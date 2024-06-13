import Foundation

func solution(_ polynomial:String) -> String {
    var xCounter: Int = 0
    var numCounter: Int = 0
    var arr = polynomial.split(separator: " ").map{String($0)}
    var numArr = arr.filter { $0.isNumber() }
    var xArr = arr.filter { $0.contains("x") }
    print(numArr)
    print(xArr)

    return ""
}