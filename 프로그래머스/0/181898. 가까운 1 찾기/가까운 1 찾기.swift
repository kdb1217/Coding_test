import Foundation

func solution(_ arr:[Int], _ idx:Int) -> Int {
    return arr.indices.firstIndex(where: {arr[$0] == 1 && $0 >= idx }) ?? -1
}