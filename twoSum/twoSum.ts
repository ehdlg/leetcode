// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

function twoSum(nums: number[], target: number): number[] {
  const map = new Map();

  for (let i = 0; i < nums.length - 1; i++) {
    const number = nums[i];
    const diff = target - number;
    const mapValue = map.get(diff);

    if (null != mapValue) return [i, mapValue];

    map.set(number, i);
  }

  return [];
}
