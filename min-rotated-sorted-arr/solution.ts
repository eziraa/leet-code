function findMin(nums: number[]): number {
    
    if (nums.length < 1 || nums.length > 5000) return 0;
    if (nums.some((num) => num < -5000 || num > 5000)) return 0;
    if (nums.length === 1) return nums[0];


    for (let i = 0; i < nums.length-1; i++)
    {
        if ((nums[i + 1] - nums[i]) < 0) 
            return nums[i + 1];
    }

    return nums[0];
};