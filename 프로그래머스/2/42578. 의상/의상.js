function solution(clothes) {    
    let map = {}
    let answer = 1
    
    clothes.forEach(([item, category]) => {
        if (!map[category]) map[category] = []
        map[category].push(item)
    })
    
    Object.values(map).forEach((item) => {
        answer *= (item.length + 1)
    })
    
    return answer - 1
}