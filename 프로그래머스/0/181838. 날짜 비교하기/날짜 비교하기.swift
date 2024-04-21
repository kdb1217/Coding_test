import Foundation

func solution(_ date1:[Int], _ date2:[Int]) -> Int {
    return Int(date1.map{String($0)}.joined())! >= Int(date2.map{String($0)}.joined())! ? 0 : 1
}