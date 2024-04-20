import Foundation

func solution(_ binomial:String) -> Int {
    let arr = binomial.split(separator: " ").map {String($0)}
    if arr[1] == "+" {
        return Int(arr[0])! + Int(arr[2])!
    } else if arr[1] == "-" {
        return Int(arr[0])! - Int(arr[2])!
    } else {
        return Int(arr[0])! * Int(arr[2])!
    }
}