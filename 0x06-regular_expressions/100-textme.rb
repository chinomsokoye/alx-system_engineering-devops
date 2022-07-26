#!/usr/bin/env ruby
# Matches sender, receiver, flags in textme

puts ARGV[0].scan(/(?<=from:)\S*(?<!\])|(?<=to:).?\d{10,11}|(?<=flags:)\S*(?<!\])/).join(',')
