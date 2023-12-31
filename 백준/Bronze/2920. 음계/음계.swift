import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

var ascending: [Int] = input.sorted()
var descending: [Int] = input.sorted(by: >)

if (input == ascending) {
    print("ascending")
}
else if (input == descending) {
    print("descending")
}
else {
    print("mixed")
}
