# frozen_string_literal: true

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, _next = nil)
    @val = val
    @next = _next
  end
end

def merge_two_lists(list1, list2)
  arr = []

  while list1 && list2
    if list1.val <= list2.val
      arr.push list1.val
      list1 = list1.next
    else
      arr.push list2.val
      list2 = list2.next
    end
  end

  while list1
    arr.push list1.val
    list1 = list1.next
  end

  while list2
    arr.push list2.val
    list2 = list2.next
  end

  arr
end
