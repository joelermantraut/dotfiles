alias ls='exa -l'
alias la='exa -la'
alias lg='exa -la --git-ignore'
alias ld='exa -l -D'
alias Ls='exa -l' # common typo error
alias tree='exa --tree --level=2 -l'
alias cls='clear && ls'

alias wm_class='xprop WM_CLASS'
alias wm_name='xprop WM_NAME'

alias addmic='pacmd load-module module-alsa-source device=hw:Loopback,1,0'

alias t='trans en:es'
alias T='trans es:en'

alias ps='procs --tree'

alias v='nvim'

alias cpp='pwd | xsel -b'

alias alacritty='snap run alacritty'

alias rm='trash'

alias bat='batcat --theme catppuccin_mocha'
alias cat='bat'
