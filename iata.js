

//convention: All lower-case!
const airlines = { "aa":"american airlines", "ua":"united airlines", "dl":"delta" }

//
function IATAsearch(AL){
    
    if (AL.length == 2){
        //input IATA two-letter code, output airline name
        if (airlines[AL.toLowerCase()] != undefined )
        {return airlines[AL.toLowerCase()]}
        
    } else if (AL.length > 3){
        //input airline name, output two-letter code
        let keyName = ''
        Object.keys(airlines).forEach(prop=> {if (airlines[prop] ==  AL.toLowerCase()) keyName=prop})
        return  keyName;
        
    }
}

console.log(IATAsearch('ua'))
console.log(IATAsearch("American Airlines"))






///hgiust simp

// function IATAsearch(twoLetter){
//     //input IATA two-letter code, output Whole name
//     if (airlines[twoLetter.toLowerCase()] != undefined )
//         {return airlines[twoLetter.toLowerCase()]}
    
// }


// const input = 'American Airlines'
// const ybn  =  []
// Object.keys(airlines).forEach(AL=> {if (airlines[AL] ==  input) ybn.push(AL)})
// console.log(ybn);

//console.log(Object.keys(airlines)[Object.indexOf('United Airlines', airlines)]);
// function IATAencode(){
    //     if (Object.keys(airlines)[twoLetter] != undefined){ return }
// }


// let lookedUp = "aa"

// console.log(airlines[lookedUp]);
// console.log(airlines["assface"]);


// console.log(IATAsearch("Aa"));
// console.log(IATAsearch("faceass"));
// console.log(IATAsearch("uA"));
// console.log(IATAsearch("DL"));