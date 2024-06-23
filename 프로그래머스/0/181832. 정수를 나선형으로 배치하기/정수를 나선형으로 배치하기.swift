import Foundation

func solution(_ n:Int) -> [[Int]] {
 var result = Array(repeating: Array(repeating: 0, count: n), count: n)
    var value = 1
    var top = 0
    var bottom = n - 1
    var left = 0
    var right = n - 1
    
    while top <= bottom && left <= right {
        for i in left...right {
            result[top][i] = value
            value += 1
        }
        top += 1
        
        for i in top...bottom {
            result[i][right] = value
            value += 1
        }
        right -= 1
        
        if top <= bottom {
            for i in (left...right).reversed() {
                result[bottom][i] = value
                value += 1
            }
            bottom -= 1
        }
        
        if left <= right {
            for i in (top...bottom).reversed() {
                result[i][left] = value
                value += 1
            }
            left += 1
        }
    }
    
    return result
}