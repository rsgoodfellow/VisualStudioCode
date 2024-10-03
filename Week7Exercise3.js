let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; //declares and initializes array

console.log("All Array Elements: "); //dispalys text
console.log(nums.join(", ")); //displays array element and prints a comma and space after each element

let sum = 0; //declares and initalizes sum integer
for (let i = 0; i < nums.length; i++) //for loop to loop through each index of nums
{
    sum += nums[i]; //adds the number in the index to sum int
}

console.log("Sum of all elements: " + sum); //displays sum

let max = 0; //declares and initializex max variable
let min = 100;  //declares and initializex min variable

for (let i = 0; i < nums.length; i++) //for loop to loop through each index
{
    if (nums[i] > max) //if statement to check if the number in the index is greater than the max variable
    {
        max = nums[i]; //sets the max number to the number in the index
    }
}

for (let i = 0; i < nums.length; i++) //for loop to loop through each index
{
    if (nums[i] < min)  //if statement to check if the number in the index is less than the min variable
    {
        min = nums[i]; //sets the min number to the number in the index
    }
}

console.log("Max = " + max); //displays max
console.log("Min = " + min); //displays min

// Reverse the array and print the reversed array
let reversedNums = nums.reverse(); //sets new array equal to the reverse of the nums array
console.log("Reversed array:"); //displays text
console.log(reversedNums.join(", "));  //displays array element and prints a comma and space after each element
