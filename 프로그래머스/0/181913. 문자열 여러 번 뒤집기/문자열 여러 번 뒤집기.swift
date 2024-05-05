import Foundation

func solution(_ my_string:String, _ queries:[[Int]]) -> String {
    var arr = my_string.map {String($0)}
    for i in queries {
        var j = i[0]
        var k = i[1]
        while j < k {
            arr.swapAt(j,k)
            j += 1
            k -= 1
        }
    }
    return arr.joined()
}