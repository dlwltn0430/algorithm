function solution(phone_book) {
    let phoneNumber = {}
    
    for (const num of phone_book) {
        phoneNumber[num] = true
    }
    
    for (let i = 0; i < phone_book.length; i++) {
        for (let j = 1; j < phone_book[i].length; j++) {
            const prefix = phone_book[i].slice(0, j)
            if (phoneNumber[prefix]) return false
        }
    }
    
    return true
}