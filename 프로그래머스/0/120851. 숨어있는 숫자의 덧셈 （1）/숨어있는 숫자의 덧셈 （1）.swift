import Foundation

func solution(_ my_string:String) -> Int {
    var arr: [String] = my_string.map{ String($0) }
    var tmp = arr.filter {$0.isNumber}
    print(tmp)
    return 0
}