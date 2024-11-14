function twoSum(nums: number[], target: number): number[] {
    

    if (nums.length < 2 || nums.length > 10000)
    {
        return []
    }
    if (target < -1000000000 || target > 1000000000) return [];
    for (let i = 0; i < nums.length; i++)
    {
        for (let j = i + 1; j < nums.length; j++)
        {
            if (nums[i] + nums[j] === target)
            {
                return [i, j]
            }
        }
    }
    return []
};