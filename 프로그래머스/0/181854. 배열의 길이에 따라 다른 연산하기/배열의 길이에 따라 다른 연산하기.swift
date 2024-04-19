import Foundation

func solution(_ arr:[Int], _ n:Int) -> [Int] {
    if arr.count % 2 == 1 {
        return arr.indices.map {$0 % 2 == 0 ?  arr[$0] + n : arr[$0]}
    } else {
        return arr.indices.map {$0 % 2 == 1 ? arr[$0] + n: arr[$0]}
    }
}