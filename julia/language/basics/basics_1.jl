               _
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.0.0 (2018-08-08)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |


julia> isequal(NaN,NaN)
true

julia> NaN == NaN
false

# complex number 
julia> im
im

julia> (1 + 2im)*(2 - 3im)
8 + 1im

julia> sqrt(9)
3.0

julia> sqrt(-1)
ERROR: DomainError with -1.0:
sqrt will only return a complex result if called with a complex argument. Try sqrt(Complex(x)).
Stacktrace:
 [1] throw_complex_domainerror(::Symbol, ::Float64) at .\math.jl:31
 [2] sqrt at .\math.jl:479 [inlined]
 [3] sqrt(::Int64) at .\math.jl:505
 [4] top-level scope at none:0


julia> sqrt(im)
0.7071067811865476 + 0.7071067811865475im


julia> real(2 -3im)
2

julia> imag(2 -3im)
-3

julia> a = 1; b = 2; a + b*im
1 + 2im

julia> complex(a,b)
1 + 2im

julia> 6//2
3//1

julia> sin(0)
0.0

julia> cos(0)
1.0

julia> log(0)
-Inf

julia> log(1)
0.0

julia> log(10)
2.302585092994046

julia>






















































































