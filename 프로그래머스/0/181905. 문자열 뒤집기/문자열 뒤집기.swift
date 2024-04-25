import Foundation

func solution(_ my_string:String, _ s:Int, _ e:Int) -> String {
    var arr = my_string.map {String($0)}
    var cnt = 0
    var start = s
    var last = e
    while start <= last {
        arr.swapAt(start, last)
        start += 1
        last -= 1
    }
    return arr.joined()
}