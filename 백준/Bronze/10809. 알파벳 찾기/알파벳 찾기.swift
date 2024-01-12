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


let input = Array(readLine()!)
var alpha: [Int] = Array(repeating: -1, count: 26)
var answer: String = ""
var idx: Int = 0

for i in input {
    if alpha[Int(i.asciiValue! - 97)] == -1 {
        alpha[Int(i.asciiValue! - 97)] = idx
    }
    idx += 1
}

for j in 0...alpha.count - 1 {
    answer += "\(alpha[j]) "
}

print(answer)


