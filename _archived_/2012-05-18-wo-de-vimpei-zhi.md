---
layout: post
title: "我的vim配置"
date: 2012-05-18 23:22
---
用vim也有段时间了，配置什么的都是按需实现的，虽然网上有很多牛X的配置文件，但我还是觉得适合自己的才是最好的，所以日积月累，我的vim及其配件也就成了现在这个样子。

废话不多说，下面是我的`~/.vimrc`，安装了`ctags`跟`cscope`，插件的话只用了`NERD_commenter`跟`taglist`，其他的话注释都写得还算完整，希望对大家有所帮助。

```vim
""""""""""""""""""""""""
" 基础配置
""""""""""""""""""""""""
set number "显示行号
set helplang=cn "中文帮助
colorscheme elflord "设置配色
filetype plugin indent on "打开文件类型检测
syntax on "语法高亮
set statusline+=%f "在状态栏中显示文件名
set tabstop=4 "制表符为4
set shiftwidth=4 "统一缩进为4
set autoindent "vim使用自动对齐，也就是把当前行的对起格式应用到下一行
set smartindent "依据上面的对起格式，智能的选择对起方式
set showmatch "设置匹配模式，类似当输入一个左括号时会匹配相应的那个右括号
set incsearch "在输入要搜索的文字时，vim会实时匹配
set hlsearch "高亮显示搜索的内容
""""""""""""""""""""""""
" 中文编码
""""""""""""""""""""""""
"set fileencodings=gb2312,gb18030,utf-8
"set termencoding=utf-8
"set encoding=prc
""""""""""""""""""""""""
" 一键编译/运行，F5编译，F6执行，支持C/C++/Java/Python
""""""""""""""""""""""""
func! CompileGcc()
exec "w"
let compilecmd="!gcc "
let compileflag="-o %< "
if search("mpi\.h") != 0
let compilecmd = "!mpicc "
endif
if search("glut\.h") != 0
let compileflag .= " -lglut -lGLU -lGL "
endif
if search("cv\.h") != 0
let compileflag .= " -lcv -lhighgui -lcvaux "
endif
if search("omp\.h") != 0
let compileflag .= " -fopenmp "
endif
if search("math\.h") != 0
let compileflag .= " -lm "
endif
exec compilecmd." % ".compileflag
endfunc
func! CompileGpp()
exec "w"
let compilecmd="!g++ "
let compileflag="-o %< "
if search("mpi\.h") != 0
let compilecmd = "!mpic++ "
endif
if search("glut\.h") != 0
let compileflag .= " -lglut -lGLU -lGL "
endif
if search("cv\.h") != 0
let compileflag .= " -lcv -lhighgui -lcvaux "
endif
if search("omp\.h") != 0
let compileflag .= " -fopenmp "
endif
if search("math\.h") != 0
let compileflag .= " -lm "
endif
exec compilecmd." % ".compileflag
endfunc
 
func! RunPython()
exec "!python2 %"
endfunc
func! CompileJava()
exec "!javac %"
endfunc
 
 
func! CompileCode()
exec "w"
if &filetype == "cpp"
exec "call CompileGpp()"
elseif &filetype == "c"
exec "call CompileGcc()"
elseif &filetype == "python"
exec "call RunPython()"
elseif &filetype == "java"
exec "call CompileJava()"
endif
endfunc
 
func! RunResult()
exec "w"
if search("mpi\.h") != 0
exec "!mpirun -np 4 ./%<"
elseif &filetype == "cpp"
exec "! ./%<"
elseif &filetype == "c"
exec "! ./%<"
elseif &filetype == "python"
exec "call RunPython"
elseif &filetype == "java"
exec "!java %<"
endif
endfunc
 
map <F5> :call CompileCode()<CR>
imap <F5> <ESC>:call CompileCode()<CR>
vmap <F5> <ESC>:call CompileCode()<CR>
 
map <F6> :call RunResult()<CR>
""""""""""""""""""""""""
" ctags设置
""""""""""""""""""""""""
map <F12> :!ctags -R <CR><CR> "按下F12即可生成tag
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" cscope设置
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <F7> :!cscope -Rb <CR><CR> "按下F7即可生成cscope.out
if has("cscope")
set csprg=/usr/bin/cscope
set csto=1
set cst
set nocsverb
" add any database in current directory
if filereadable("cscope.out")
cs add cscope.out
endif
set csverb
endif
 
nmap <C-@>s :cs find s <C-R>=expand("<cword>")<CR><CR>
nmap <C-@>g :cs find g <C-R>=expand("<cword>")<CR><CR>
nmap <C-@>c :cs find c <C-R>=expand("<cword>")<CR><CR>
nmap <C-@>t :cs find t <C-R>=expand("<cword>")<CR><CR>
nmap <C-@>e :cs find e <C-R>=expand("<cword>")<CR><CR>
nmap <C-@>f :cs find f <C-R>=expand("<cfile>")<CR><CR>
nmap <C-@>i :cs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
nmap <C-@>d :cs find d <C-R>=expand("<cword>")<CR><CR>
""""""""""""""""""""""""
" taglist设置
""""""""""""""""""""""""
map <F3> :silent! Tlist<CR> "按下F3就可以呼出了
let Tlist_Show_One_File = 1 "不同时显示多个文件的tag，只显示当前文件的
let Tlist_Exit_OnlyWindow = 1 "当taglist是最后一个分割窗口时，自动退出vim
""""""""""""""""""""""""
" NERD_commenter的设置
""""""""""""""""""""""""
map <c-x> \c<space> "按下ctrl+c即可添加/取消注释
```
