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

while true {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    if input[0] + input[1] == 0 {
        break
    }
    else {
        answerArr.append(input[0] + input[1])
    }
}

for i in 0...answerArr.count - 1{
    print(answerArr[i])
}
