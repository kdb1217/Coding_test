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

var answerArr: [Int] = []

while let input = readLine() {
    let num = input.split(separator: " ").map{Int($0)! }
    answerArr.append(num[0] + num[1])
}

for i in 0...answerArr.count - 1{
    print(answerArr[i])
}
