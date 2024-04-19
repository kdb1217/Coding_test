import Foundation

func solution(_ num_list:[Int]) -> Int {
    let odd: Int = num_list.indices.filter {$0 % 2 == 0}.map {Int(num_list[$0])}.reduce(0, +)
    let even: Int = num_list.indices.filter {$0 % 2 == 1}.map {Int(num_list[$0])}.reduce(0, +)
    return odd > even ? odd : even
}