# looking for missing values

julia> v = [1, 2, missing, 4]
4-element Array{Union{Missing, Int64},1}:
 1
 2
  missing
 4

julia> ismissing.(v)
4-element BitArray{1}:
 false
 false
  true
 false

julia>
