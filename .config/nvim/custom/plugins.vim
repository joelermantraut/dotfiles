call plug#begin()

" Themes 
Plug 'sainnhe/sonokai'
Plug 'jacoborus/tender.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'ayu-theme/ayu-vim'
Plug 'morhetz/gruvbox'

" Files 
Plug 'preservim/nerdtree' " NERDTree
Plug 'ryanoasis/vim-devicons'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim' " FZF
Plug 'mbbill/undotree'
Plug 'jeetsukumaran/vim-buffergator' " To manage buffers

" Formatting 
Plug 'frazrepo/vim-rainbow' " Shows rainbow brackets and others 
"Plug 'preservim/nerdcommenter' " Comments Code
Plug 'tpope/vim-commentary'
Plug 'chrisbra/colorizer' " Shows colors with colors 
Plug 'lfilho/cosco.vim' " To autocomplete comma and semicolon
Plug 'tpope/vim-repeat' " To make repeat more clever
Plug 'raimondi/delimitmate' " To auto close brackets, etc
Plug 'tpope/vim-surround' " Does easy to replace quoting, brackets, etc.
Plug 'Yggdroot/indentLine' " Shows un indent line

" Syntax Highlighting
Plug 'sheerun/vim-polyglot'

" Interfaz
Plug 'itchyny/lightline.vim' " Status Bar 
Plug 'KabbAmine/vCoolor.vim' " Color Selector
Plug 'voldikss/vim-floaterm'
Plug 'mg979/vim-visual-multi', {'branch': 'master'}

" Codificacion
Plug 'majutsushi/tagbar'
Plug 'mattn/emmet-vim' " Emmet
Plug 'easymotion/vim-easymotion' " Search in code 
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Autocompletion 
"Plug 'sirver/ultisnips'
Plug 'itchyny/vim-gitbranch' " To show git branch in status bar
Plug 'airblade/vim-gitgutter' " To show changes in file
" Installed with Coc: coc-prettier and coc-pairs

call plug#end()
