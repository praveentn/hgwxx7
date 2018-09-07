# Arrays in Julia

# declaring an Array
julia> Array{Union{Nothing, String}}(nothing, 2)
2-element Array{Union{Nothing, String},1}:
 nothing
 nothing

# converting string to Array
julia> a = "praveen"

# collect is similar to list operation
# on strings in Python
julia> l = collect(a)
7-element Array{Char,1}:
 'p'
 'r'
 'a'
 'v'
 'e'
 'e'
 'n'

# type check
julia> typeof(l)
Array{Char,1}

# display Array
julia> l
7-element Array{Char,1}:
 'p'
 'r'
 'a'
 'v'
 'e'
 'e'
 'n'
 


