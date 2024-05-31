import Foundation

/*
풀이계획
1. 제일 큰 가로값과 제일 큰 새로값을 찾는다
2. 제일 큰 세로값이 가로값보다 가로와 새로값을 바꾼다.
3. 그대로 곱해서 리턴한다.
*/
func solution(_ sizes:[[Int]]) -> Int {
    var arr = sizes
    var maxX: Int = 0
    var maxY: Int = 0
    
    for i in 0..<sizes.count {
        if arr[i][0] > arr[i][1] {
            arr[i].swapAt(0,1)
        }
    }
    
    for i in 0..<sizes.count {
        if maxX < arr[i][0] {
            maxX = arr[i][0]
        }
        if maxY < arr[i][1] {
            maxY = arr[i][1]
        }
    }
    return maxX * maxY
}