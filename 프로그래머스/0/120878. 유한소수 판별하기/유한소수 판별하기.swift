import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    var top: Int = a // 분자
    var bottom: Int = b // 분모
    var start = 2
    while start <= min(top, bottom) {
        if (bottom == 1 || top == 1) {
            break
        }
        if bottom % start == 0 && top % start == 0 {
            bottom /= start
            top /= start
        } else {
            start += 1
        }
        if start >= bottom && start > top {
            break
        }
    }
    return isAnswer(bottom)
}

func isAnswer(_ number: Int) -> Int {
    var tmp = number
    var numbers: Set<Int> = []
    
    while true {
        if tmp == 1{
            return 1
            break
        }
        if tmp % 2 == 0 {
            tmp /= 2
        } else if tmp % 5 == 0 {
            tmp /= 5
        } else {
            return 2
            break
        }
    }
    return 1
}