import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var stock: Int = n
    var k = n
    var answer: Int = 0
    var tmp: Int = 0
    
    while (k > a) {
        tmp += (k / a) * b
        stock = k % a
        answer += tmp
        k = tmp + stock
    } 
    return answer
}