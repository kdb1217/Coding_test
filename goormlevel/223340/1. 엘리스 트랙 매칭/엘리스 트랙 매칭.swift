let N = Int(readLine()!)!
let friendsTracks = readLine()!.split(separator: " ").map { String($0) }
let myTrack = readLine()!

print(friendsTracks.filter { $0 == myTrack }.count)