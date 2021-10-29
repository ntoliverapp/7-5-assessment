// Find longest word

let arrayColors = ['Red', 'Black', 'Purple','Gold']
let arrayNames = ['Jack', 'James', 'Ignacio','Mohammed']

function findLongestWord(characters){
    let charLength = 0
    for(let i =0; i < characters.length; i++) {
        if(characters[i].length > charLength){
            charLength = characters[i].length
        }
    }
    return charLength
    }
    console.log(findLongestWord(arrayNames))

//Pangram sentence

let a = "Guitar Hero"
let b = "String"

function isPangram(string){
    for(let i =0; i < string.length; i++) {
        if(string.count > 1){
            return false
        } else{
            return true
        }
}}

console.log(isPangram(b))