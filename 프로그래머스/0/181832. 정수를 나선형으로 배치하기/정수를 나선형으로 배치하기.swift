import Foundation

func solution(_ n:Int) -> [[Int]] {
    var x = Array((0..<n))
    var y = Array((0..<n).reversed())
    var arr = Array(repeating: Array(repeating: 0, count: n), count: n)
    var count = 1
    while true {
        for i in x {
            arr[y.last!][i] = count
            count += 1
        }
        if count >= n*n { 
            break 
        }
        y.removeLast()
        y.reverse()

        for i in y {
            arr[i][x.last!] = count
            count += 1
        }
        x.removeLast()
        x.reverse()
    }
    return arr
}