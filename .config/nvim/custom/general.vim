syntax on
set number
set mouse=a " Enables mouse interaction 
set sidescroll=1
set noerrorbells 
set expandtab " TABs are space 
set sw=4 
set tabstop=4
set softtabstop=4
set smartindent
" This sets the TAB width and configures 
set numberwidth=1 " Optimizes left width
set nobackup
set nowritebackup
set noswapfile
set undodir=~/.config/nvim/undodir
set undofile
set nowrap
set incsearch " Search is done while writing 
set smartcase  
set encoding=utf-8
set cursorline " Enables the right limit bar
set colorcolumn=120 " And sets the position 
set nolist " To not show special characters
set updatetime=10 " Screen refresh time 
set timeoutlen=500 " Leader key wait time 
set hidden " Hides tabs (windows) not in use
set clipboard=unnamedplus
" With this vim uses primary clipboard
set guicursor= " Cursor is always a block
set nohlsearch
set scrolloff=10 " Centers the cursor when near EOF
set signcolumn=yes " Use for linters and git apps
set noshowmode " To avoid showing --INSERT-- and so
set encoding=UTF-8

set cmdheight=2 " More space for messages

set shortmess+=c " Don't pass messages to completion menu
set shortmess+=F

filetype plugin on
filetype plugin indent on

set whichwrap+=>,l
set whichwrap+=<,h
" To overflow to the last or the previous
" line when press arrows

let mapleader = " "
" Tecla modificadora (leader)
