rcc = {}
rcc["="] = 1 << 0
rcc[">"] = 1 << 1
rcc["<"] = 1 << 2
rcc["!"] = 1 << 3
rcc["o"] = 1 << 4
rcc["=>"] = 1 << 0 | 1 << 1
rcc["=<"] = 1 << 0 | 1 << 2
rcc["=!"] = 1 << 0 | 1 << 3
rcc["=o"] = 1 << 0 | 1 << 4
rcc["><"] = 1 << 1 | 1 << 2
rcc[">!"] = 1 << 1 | 1 << 3
rcc[">o"] = 1 << 1 | 1 << 4
rcc["<!"] = 1 << 2 | 1 << 3
rcc["<o"] = 1 << 2 | 1 << 4
rcc["!o"] = 1 << 3 | 1 << 4
rcc["=><"] = 1 << 0 | 1 << 1 | 1 << 2
rcc["=>!"] = 1 << 0 | 1 << 1 | 1 << 3
rcc["=>o"] = 1 << 0 | 1 << 1 | 1 << 4
rcc["=<!"] = 1 << 0 | 1 << 2 | 1 << 3
rcc["=<o"] = 1 << 0 | 1 << 2 | 1 << 4
rcc["=!o"] = 1 << 0 | 1 << 3 | 1 << 4
rcc["><!"] = 1 << 1 | 1 << 2 | 1 << 3
rcc["><o"] = 1 << 1 | 1 << 2 | 1 << 4
rcc[">!o"] = 1 << 1 | 1 << 3 | 1 << 4
rcc["<!o"] = 1 << 2 | 1 << 3 | 1 << 4
rcc["=><!"] = 1 << 0 | 1 << 1 | 1 << 2 | 1 << 3
rcc["=><o"] = 1 << 0 | 1 << 1 | 1 << 2 | 1 << 4
rcc["=>!o"] = 1 << 0 | 1 << 1 | 1 << 3 | 1 << 4
rcc["=<!o"] = 1 << 0 | 1 << 2 | 1 << 3 | 1 << 4
rcc["><!o"] = 1 << 1 | 1 << 2 | 1 << 3 | 1 << 4
rcc["=><!o"] = 1 << 0 | 1 << 1 | 1 << 2 | 1 << 3 | 1 << 4