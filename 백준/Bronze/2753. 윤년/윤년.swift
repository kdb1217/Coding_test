import Foundation

let input = Int(readLine()!)!

if input % 4 == 0 {
    if input % 100 != 0 || input % 400 == 0 {
        print("1")
    }
    else {
        print("0")
    }
}
else {
    print("0")
}
