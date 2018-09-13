# using packages

# Pkg is designed around "environments"
# this significantly reduces dependencies

julia> Pkg.status()
ERROR: UndefVarError: Pkg not defined
Stacktrace:
 [1] top-level scope at none:0

# enter ']' on the julia repl to go to 'pkg' prompt

julia> ]

# adding the package 'Example' to the current project
(v1.0) pkg> add Example
 Resolving package versions...
 Installed Example ─ v0.5.1
  Updating `C:\Users\praveen\.julia\environments\v1.0\Project.toml`
  [7876af07] + Example v0.5.1
  Updating `C:\Users\praveen\.julia\environments\v1.0\Manifest.toml`
  [7876af07] + Example v0.5.1
  [2a0f44e3] + Base64
  [8ba89e20] + Distributed
  [b77e0a4c] + InteractiveUtils
  [8f399da3] + Libdl
  [37e2e46d] + LinearAlgebra
  [56ddb016] + Logging
  [d6f4376e] + Markdown
  [9a3f8284] + Random
  [9e88b42a] + Serialization
  [6462fe0b] + Sockets
  [8dfed614] + Test

# manifest: manifest status, includes the dependencies of explicitly added packages

# loading a package in julia
(v1.0) pkg> ^C

julia> using Example
[ Info: Precompiling Example [7876af07-990d-54b4-ab0e-23690620f79a]

julia>

julia> Example.hello("User")
"Hello, User"

