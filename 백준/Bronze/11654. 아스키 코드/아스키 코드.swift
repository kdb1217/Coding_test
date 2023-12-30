import Foundation

let text = readLine()!
let asciiToText = Int(UnicodeScalar(text)!.value)
print(asciiToText)
