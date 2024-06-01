import Foundation
// a 빈병을 a개를 주면 b개의 콜라를 준다.
// b 빈병 a개를 줬을때 다시 받는 콜라의 수
func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var CokeCount: Int = 0
    var emptiedBottle: Int = n
    
    while true {
        if emptiedBottle >= a {
            emptiedBottle = emptiedBottle - a
            emptiedBottle += b
            CokeCount += b
        } else {
            break
        }
    }
    return CokeCount
}