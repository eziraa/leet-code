function maxProduct(nums: number[]): number {
    

    if (nums.length < 1 || nums.length > 20000) return 0;
    if (nums.length === 1) return nums[0];
    let max = 0;
    for (let i = 1; i < nums.length; i++)
    {
        if (nums[i] > 10 || nums[i] < -10) return 0;
       max = Math.max(max,nums[i] * nums[i-1]);
    }
    return max;
};