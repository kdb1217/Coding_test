import Foundation

func solution(_ my_string:String) -> String {
    let arr = ["a","e","i","o","u"]
    return my_string.map { String($0) }.filter { !arr.contains($0) }.joined()
}