import Foundation

func solution(_ letter:String) -> String {
    var arr = letter.split(separator: " ")
    var answer = ""
    let morse: [String: Character] = [
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f",
    "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
    "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
    "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
    "-.--": "y", "--..": "z"
    ]
    for i in arr {
        var tmp = String(i)
        answer += String(morse[tmp]!)
    }
    return answer
}