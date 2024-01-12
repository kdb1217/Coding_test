//
import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}


var input = readLine()!
input = input.uppercased()

var inputArr: [Character] = []

for i in input {
    inputArr.append(i)
}
var cnt = [Character: Int]()

inputArr.forEach {
    cnt[$0, default: 0] += 1
}

cnt = cnt.filter { $0.value == cnt.values.max()! }

cnt.count > 1 ? print("?") : print(cnt.keys.first!)

