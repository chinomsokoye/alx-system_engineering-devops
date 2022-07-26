#!/usr/bin/env ruby
# Matches sender, receiver, flags in textme

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]\).join(',')
