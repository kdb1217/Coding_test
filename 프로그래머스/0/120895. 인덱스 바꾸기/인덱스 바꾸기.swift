import Foundation

func solution(_ my_string:String, _ num1:Int, _ num2:Int) -> String {
    var arr = my_string.map {String($0)}
    let tmp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = tmp
    return arr.joined()
}

