import Foundation

func solution(_ my_string:String) -> [Int] {
    var alphabet: [Int] = Array(repeating: 0, count:52)
    for i in my_string {
        if i.asciiValue! <= Character("Z").asciiValue! {
            alphabet[Int(i.asciiValue!) - 65] += 1
        } else {
            alphabet[Int(i.asciiValue!) - 71] += 1
        }
    }
    return alphabet
}