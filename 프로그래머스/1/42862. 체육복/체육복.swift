import Foundation

/* 
    풀이 계획
*/
func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var arr:[Int: Int] = [:]
    for i in 1...n {
        arr[i] = 1
        if reserve.contains(i) {
             arr[i]! += 1
        } 
        if lost.contains(i) {
            arr[i]! -= 1
        }
    }
    for i in 1...n {
        if i == 2 {
            if arr[i]! > 1 && arr[i - 1]! == 0 {
                arr[i]! -= 1
                arr[i - 1]! += 1
            }
        }
        if arr[i]! == 2 {
            if i > 1 {
                if arr[i - 1]! == 0 {
                    arr[i - 1]! += 1
                    arr[i]! -= 1  
                }
            }
            if arr[i]! == 2 && i < n  {
                if arr[i + 1]! == 0 {
                    arr[i + 1]! += 1
                    arr[i]! -= 1 
                }
            }
        } 
    }
    if arr[n]! == 2 && arr[n - 1] == 0 {
            arr[n]! -= 1
            arr[n-1]! += 1
    }
    print(arr)
    return arr.keys.filter { arr[$0]! > 0 }.count
}