function countEven(numbers) {
    let result = 0
    for (let x of numbers) {
        if (x % 2 == 0) result++
    }
    return result
}

console.log(countEven([1, 2, 4]))