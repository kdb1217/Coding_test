import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

var answerArr: [Int] = input.map {$0 * $0}
let answer = answerArr.reduce(0) {$0 + $1} % 10
print(answer)
