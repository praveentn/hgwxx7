# using strings in Julia
# Julia command line

julia> a = "praveen"

julia> a[1]
'p': ASCII/Unicode U+0070 (category Ll: Letter, lowercase)

# index starts at 1!

# for loop in Julia
julia> for i in a
           println(i)
       end

p
r
a
v
e
e
n

# no indentations unlike Python ;)

# collect(<string>)
julia> collect(a)
7-element Array{Char,1}:
 'p'
 'r'
 'a'
 'v'
 'e'
 'e'
 'n'
 
# isvalid.()
julia> isvalid.(collect(a))
7-element BitArray{1}:
 true
 true
 true
 true
 true
 true
 true

