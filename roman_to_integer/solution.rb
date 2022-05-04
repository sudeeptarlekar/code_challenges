# frozen_string_literal: true
require 'pry'

def roman_to_int(s)
  map = {
    'I' => 1,
    'IV' => 4,
    'V' => 5,
    'IX' => 9,
    'X' => 10,
    'XL' => 40,
    'L' => 50,
    'XC' => 90,
    'C' => 100,
    'CD' => 400,
    'D' => 500,
    'CM' => 900,
    'M' => 1000,
  }

  len = s.length - 1
  sum = 0

  while len >= 0
    if len != 0 && map[s[len]] > map[s[len - 1]]
      sum += map["#{s[len - 1]}#{s[len]}"]
      len -= 1
    else
      sum += map[s[len]]
    end
    len -= 1
  end
  
  sum
end

roman_to_int('MCMXCIV')
