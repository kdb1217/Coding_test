import Foundation

func solution(_ order:[String]) -> Int {
    var cheap: [String] = ["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]
    var expensive: [String] = ["icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot","cafelatte"]
    var total: Int = 0
    total += order.filter {cheap.contains($0)}.count * 4500
    total += order.filter {expensive.contains($0)}.count * 5000
    return total
}