# frozen_string_literal: true
require 'pry'

def int_to_roman(num)
  map = {
    'M' => 1000,
    'CM' => 900,
    'D' => 500,
    'CD' => 400,
    'C' => 100,
    'XC' => 90,
    'L' => 50,
    'XL' => 40,
    'X' => 10,
    'IX' => 9,
    'V' => 5,
    'IV' => 4,
    'I' => 1,
  }

  output = ''

  map.each do |roman, decimal|
    next if num < decimal

    r = num / decimal
    output += roman * r
    num -= decimal * r
  end

  output
end

int_to_roman(20)
