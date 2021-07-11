# frozen_string_literal: true

class Node
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

class Solution
  def add_two_numbers(node1, node2)
    answer_node = Node.new
    current_node = answer_node
    carry = 0

    while node1 || node2 do
      sum = node1&.val + node2&.val + carry
      carry = (sum/10).to_i

      current_node.next = Node.new(sum % 10)
      current_node = current_node.next

      node1 = node1&.next
      node2 = node2&.next
    end

    current_node.next = Node.new(carry) if carry > 0

    answer_node.next
  end
end
