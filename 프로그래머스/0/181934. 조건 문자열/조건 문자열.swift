import Foundation

func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    if eq == "!" {
        if ineq == "<" {
            return n < m ? 1 : 0
        } else {
            return n > m ? 1 : 0
        }
    } else {
        if ineq == "<" {
            return n <= m ? 1 : 0
        } else {
            return n >= m ? 1 : 0
        }
    }
}