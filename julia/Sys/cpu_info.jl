# cpu info
# executed from command line
# julia> is the prompt

# cpu summary
julia> Sys.cpu_summary
cpu_summary (generic function with 3 methods)

julia> Sys.cpu_summary()
Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz:
       speed         user         nice          sys         idle          irq
#1  2496 MHz   70265296            0     52962390    1452947656      2625906  ticks
#2  2496 MHz   62610218            0     74936468    1438628203     22954593  ticks
#3  2496 MHz   72306906            0     52867046    1451000937       942187  ticks
#4  2496 MHz   67773812            0     43695703    1464705359      1063671  ticks

# cpu info
julia> Sys.cpu_info()
4-element Array{Base.Sys.CPUinfo,1}:
 Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz:
        speed         user         nice          sys         idle          irq
     2496 MHz   70256484            0     52955265    1452763812      2625656  ticks
 Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz:
        speed         user         nice          sys         idle          irq
     2496 MHz   62601796            0     74927593    1438445718     22952421  ticks
 Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz:
        speed         user         nice          sys         idle          irq
     2496 MHz   72298156            0     52859765    1450817187       942046  ticks
 Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz:
        speed         user         nice          sys         idle          irq
     2496 MHz   67762500            0     43689281    1464523312      1063468  ticks

julia> Sys.CPU_THREADS
4

julia> Sys.CPU_NAME
"skylake"

julia> Sys.uptime()
7.2779536887234e6

julia> Sys.free_memory()
0x00000001d4ba9000

julia> Sys.ARCH
:x86_64

julia> Sys.MACHINE
"x86_64-w64-mingw32"

julia> Sys.total_memory()
0x00000002f7b02000

julia> Sys.KERNEL
:NT

julia> Sys.iswindows()
true

julia> Sys.islinux()
false

julia> Sys.isunix()
false

julia> Sys.loadavg()
3-element Array{Float64,1}:
 0.0
 0.0
 0.0

julia>


  


