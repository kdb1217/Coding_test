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

let input = Int(readLine()!)!
var answer: [Int] = []
for _ in 0...input - 1 {
    let nums = readLine()!.split(separator: " ").map { Int(String($0))! }
    answer.append(sum(a: nums[0], b: nums[1]))
}

for i in 0...input - 1 {
    print(answer[i])
}

private func sum (a: Int, b: Int) -> Int {
    return a + b
}