function encodeText(text) {
    let encodedText = "";
    for (let i = 0; i < text.length; i++) {
        let char = text.charAt(i);
        if (char.match(/[a-z]/i)) {
            if (char === 'a') {
                encodedText += 'z';
            } else if (char === 'A') {
                encodedText += 'Z';
            } else {
                encodedText += String.fromCharCode(char.charCodeAt(0) - 1);
            }
        } else {
            encodedText += char;
        }
    }
    return encodedText;
}

let userInput = prompt("Enter the text to encode:");
let encodedText = encodeText(userInput);
console.log("Encoded text:", encodedText);
