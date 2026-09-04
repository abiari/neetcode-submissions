class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        sequences = {}
        current_seq = 1
        for i in range(len(nums)):
            if i == 0:
                sequences[current_seq] = set([nums[i]])
                continue
            if nums[i] - 1 == nums[i - 1] or nums[i] == nums[i - 1]:
                sequences[current_seq].add(nums[i])
                continue
            current_seq += 1
            sequences[current_seq] = set([nums[i]])
        longest_sequence = 0
        for k, v in sequences.items():
            if len(v) > longest_sequence:
                longest_sequence = len(v)
        return longest_sequence
        