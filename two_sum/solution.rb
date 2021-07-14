# frozen_string_literal: true

class Solution
  def two_sum(nums, target)
    checked = {}

    nums.each_with_index do |num, index|
      diff = target - num
      return [checked[diff], index] if checked[diff]

      checked[num] = index
    end
  end
end
