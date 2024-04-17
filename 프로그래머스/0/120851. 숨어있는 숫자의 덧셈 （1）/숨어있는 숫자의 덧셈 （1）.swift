import Foundation

func solution(_ my_string:String) -> Int {
    return my_string.filter {$0.isNumber}.reduce(0) {$0 + Int(String(($1)))!}
}