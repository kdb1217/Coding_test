import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

var hour: Int = input[0]
var min: Int = input[1]
var tmp: Int = 0
if (min - 45 < 0 ){
    tmp = min - 45
    min = 60 + tmp
    if hour == 0 {
        hour = 23
    }
    else if (hour != 0){
        hour -= 1
    }
}
else {
    min -= 45
}
print("\(hour) \(min)")

