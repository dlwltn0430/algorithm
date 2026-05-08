function solution(s){
    let a = []
    if (s[0] === ")") return false 
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(") a.push("(")
        else a.pop()
    }
    
    return a.length === 0 ? true : false
}