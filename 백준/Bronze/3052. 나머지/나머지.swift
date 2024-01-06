//
//  main.swift
//  algo
//
//  Created by 김다빈 on 12/28/23.
//
import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

//let input = readLine()!.split(separator: " ").map { Int(String($0))! }
//
//var ascending: [Int] = input.sorted()
//var descending: [Int] = input.sorted(by: >)
//
//if (input == ascending) {
//    print("ascending")
//}
//else if (input == descending) {
//    print("descending")
//}
//else {
//    print("mixed")
//}
//



var answer: [Int] = []
for _ in 1...10 {
    let num = Int(readLine()!)!
    answer.append(num)
}

var realanswer = answer.map({ (answer: Int) -> Int in
    return answer % 42
})

let a = Set(realanswer)
print(a.count)
