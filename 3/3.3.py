# Formatting Numbers for Output
# 3.3.1
x = 1234.56789

# Two decimal places of accuracy
format(x, '>10.1f')
# Left justified
format(x, '<10.1f')
# Centered
format(x, '^10.1f')
# Inclusion of thousands seperator
format(x, ',')
format(x, '0.1f')

# --
format(x, 'e')
format(x, '0.2E')

'The value is {:0,.2f}'.format(x)

# Discussion
x 
format(x, '0.1f')
format(-x, '0.1f')

# --
swap_seperators = { ord('.'):',', ord(','):'.'}
format(x, ',').translate(swap_seperators)

# --
'%0.2f' % x
'%10.1f' % x
'%-10.1f' % x

