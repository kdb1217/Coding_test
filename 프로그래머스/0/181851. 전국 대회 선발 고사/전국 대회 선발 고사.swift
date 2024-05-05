import Foundation

func solution(_ rank:[Int], _ attendance:[Bool]) -> Int {
    var array: [Int] = []
    array = rank.enumerated().filter{ attendance[$0.offset]}.map {$0.element}
    array.sort()
    print(array)
    return rank.firstIndex(of:array[0])! * 10000 + 100 * rank.firstIndex(of: array[1])! + rank.firstIndex(of: array[2])!
}