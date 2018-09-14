# Linear Algebra style
# For single linear regresion y= mx .+ b
julia> m
3.3

julia> b
2-element Array{Int64,1}:
 2
 2

julia> x
2×1 Array{Float64,2}:
 0.18541330251480792
 0.07749677781424502

julia> y = m * x .+ b
2×1 Array{Float64,2}:
 2.611863898298866
 2.2557393667870085

julia> yn = y + randn(size(y)) * 0.5
2×1 Array{Float64,2}:
 3.0183983473834095
 1.6640798029816912

julia> X = zeros(2,2)
2×2 Array{Float64,2}:
 0.0  0.0
 0.0  0.0

julia> X[:,1] = x
2×1 Array{Float64,2}:
 0.18541330251480792
 0.07749677781424502

julia> X[:,2] = 1.0
ERROR: MethodError: no method matching setindex_shape_check(::Float64, ::Int64, ::Int64)
Closest candidates are:
  setindex_shape_check(::AbstractArray{#s57,1} where #s57, ::Integer, ::Integer) at indices.jl:196
  setindex_shape_check(::AbstractArray{#s57,2} where #s57, ::Integer, ::Integer) at indices.jl:200
  setindex_shape_check(::AbstractArray, ::Integer...) at indices.jl:154
  ...
Stacktrace:
 [1] macro expansion at .\multidimensional.jl:641 [inlined]
 [2] _unsafe_setindex!(::IndexLinear, ::Array{Float64,2}, ::Float64, ::Base.Slice{Base.OneTo{Int64}}, ::Int64) at .\multidimensional.jl:636
 [3] _setindex! at .\multidimensional.jl:631 [inlined]
 [4] setindex!(::Array{Float64,2}, ::Float64, ::Function, ::Int64) at .\abstractarray.jl:998
 [5] top-level scope at none:0

julia> X[:,2] = [1.0]
ERROR: DimensionMismatch("tried to assign 1-element array to 2×1 destination")
Stacktrace:
 [1] throw_setindex_mismatch(::Array{Float64,1}, ::Tuple{Int64,Int64}) at .\indices.jl:144
 [2] setindex_shape_check at .\indices.jl:196 [inlined]
 [3] macro expansion at .\multidimensional.jl:641 [inlined]
 [4] _unsafe_setindex!(::IndexLinear, ::Array{Float64,2}, ::Array{Float64,1}, ::Base.Slice{Base.OneTo{Int64}}, ::Int64) at .\multidimensional.jl:636
 [5] _setindex! at .\multidimensional.jl:631 [inlined]
 [6] setindex!(::Array{Float64,2}, ::Array{Float64,1}, ::Function, ::Int64) at .\abstractarray.jl:998
 [7] top-level scope at none:0

julia> X[:,2] = [1.0; 1.0]
2-element Array{Float64,1}:
 1.0
 1.0

julia> X
2×2 Array{Float64,2}:
 0.185413   1.0
 0.0774968  1.0

julia> coeff_pred = X\yn
2×1 Array{Float64,2}:
 12.549686418827514
  0.6915195429433669

julia> slope =  round(coeff_pred[1], 2)
ERROR: MethodError: no method matching round(::Float64, ::Int64)
Closest candidates are:
  round(::Float64, ::RoundingMode{:Nearest}) at float.jl:368
  round(::Float64, ::RoundingMode{:Up}) at float.jl:366
  round(::Float64, ::RoundingMode{:Down}) at float.jl:364
  ...
Stacktrace:
 [1] top-level scope at none:0

julia>

slope =  round(coeff_pred[1], 2)
intercept = round(coeff_pred[2], 2)

println("The real slope is $m, and the predicted slope is $slope")
println("The real intercept is $b, and the predicted slope is $intercept")

