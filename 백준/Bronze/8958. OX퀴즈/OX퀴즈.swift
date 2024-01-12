import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}


let input = Int(readLine()!)!

private func cntScore() {
    let input = Array(readLine()!)
    var tmp: Int = 0
    var score = 0
    for i in 0...input.count-1 {
        if (input[i] == "O") {
            tmp += 1
            score += tmp
        }
        else {
            tmp = 0
            score += tmp
        }
    }
    print(score)
}


for _ in 1...input {
    cntScore()
}