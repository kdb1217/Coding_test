import Foundation

let s1 = readLine()!
print(s1.map{$0.isLowercase ? String($0).uppercased : String($0).lowercased}.joined())
