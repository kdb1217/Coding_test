let N = Int(readLine()!)!
let ableCharacters = ["a","e","i","o","u","A","E","I","O","U"]
for _ in 0..<N {
	let inputwords = readLine()!.map { String($0)}.filter { ableCharacters.contains($0) }
	if inputwords.joined() != "" {
		print(inputwords.joined())
	} else {
		print("???")
	}
}