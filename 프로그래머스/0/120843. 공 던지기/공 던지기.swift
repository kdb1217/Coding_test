import Foundation

func solution(_ numbers:[Int], _ k:Int) -> Int {
    var tmp = 0
    for i in 0..<k - 1 {
        if tmp == numbers.count - 2 {
            tmp = 0
        } else if tmp == numbers.count - 1 {
            tmp = 1
        } else {
            tmp += 2
        }
    }
    return numbers[tmp]
}