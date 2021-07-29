" General
nnoremap <leader>s :w<CR>
nnoremap <leader>q :qa<CR>
nnoremap <leader>qq :qa!<CR>
nnoremap <leader>fs :Files<CR>

" Resize windows
nnoremap <silent> <Left> :vertical resize +2<CR> 
nnoremap <silent> <Up> :resize -2<CR>
nnoremap <silent> <Down> :resize +2<CR>
nnoremap <silent> <Right> :vertical resize -2<CR>

" Tab Control
nnoremap <leader>d :bnext<CR>
nnoremap <leader>a :bprevious<CR>
nnoremap <leader>w :bdelete<CR>
" Windows
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" Syntaxis
vnoremap <expr> p '"_d"'.v:register.'p'
vnoremap <expr> P '"_d"'.v:register.'P'
" Retains clipboard after paste (not default)

nnoremap q <c-v>
" Use to enter in block visual mode
" Cannot use Ctrl+V directly because it is
" intercepted by modified terminal config

vnoremap > >gv
vnoremap < <gv
" To stay in visual mode after indent

nnoremap <leader><F5> :source $HOME/.config/nvim/init.vim<CR>
" Source Neovim config, useful when working with separated config
" files

nnoremap <leader>t :FloatermNew --height=0.8 --width=0.8 --wintype=float --autoclose=1 --position=center<CR>
" Opens a new instance of Floaterm

" Plugins
map <leader>n :NERDTreeToggle<CR>

nnoremap <leader>c :call NERDComment(0, "toggle")<CR>
vnoremap <leader>c :call NERDComment(0, "toggle")<CR>

nmap <leader>tg :TagbarToggle<CR>

map  / <Plug>(easymotion-sn)
omap / <Plug>(easymotion-tn)
nnoremap <silent> <esc> :noh<cr><esc>
" Last line not needed
" EasyMotion

vmap <leader>f <Plug>(coc-format-selected)
nmap <leader>f <Plug>(coc-format-selected)
" Format code

nnoremap <leader>ch :ColorHighlight<CR>
" Show colors with colors

nnoremap <leader>u :UndotreeToggle<CR>
" UndoTree

nnoremap <leader>b :BuffergatorToggle<CR>
" BufferGator

nnoremap <leader>, :CommaOrSemiColon<CR>
" Cosco

nnoremap <C-l> 5zl
nnoremap <C-h> 5zh
" Horizontal scroll

noremap <Leader>y "*y
noremap <Leader>p "*p
noremap <Leader>Y "+y
noremap <Leader>P "+p
