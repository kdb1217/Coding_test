import Foundation

func solution(_ hp:Int) -> Int {
    var cnt = 0
    var rest = hp
    cnt += rest / 5
    rest %= 5
    
    cnt += rest / 3
    rest %= 3
    
    cnt += rest
    
    return cnt
}