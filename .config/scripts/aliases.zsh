alias ls='exa -l'
alias la='exa -la'
alias lg='exa -la --git-ignore'
alias ld='exa -l -D'
alias tree='exa --tree --level=2 -l'
alias cls='clear && ls'

alias shutdown='shutdown -h now'
alias suspend='systemctl suspend'

alias wm_class='xprop WM_CLASS'
alias rm='trash'

alias config='/usr/bin/git --git-dir=/home/joel/.cfg/ --work-tree=/home/joel'
alias libs='/usr/bin/git --git-dir=/home/datos/Documentos/Atollic_documents/.libraries/ --work-tree=/home/datos/Documentos/Atollic_documents/'
alias winconfig='/usr/bin/git --git-dir=/home/windows/.cfg --work-tree=/home/windows'

alias passi='pass insert -e'

alias el='krusader --left .'
alias er='krusader --right .'

alias addmic='pacmd load-module module-alsa-source device=hw:Loopback,1,0'

alias t='trans en:es'
alias T='trans es:en'

alias ps='procs --tree'

alias v='nvim'

alias feh='feh --draw-filename --scale-down --borderless --action "echo %n;"'

alias yay='yay --noeditmenu --noconfirm --removemake --cleanafter --sudoloop'
# --cleanafter          Remove package sources after successful install 
# --noeditmenu          Don't edit/view PKGBUILDS
# --removemake          Remove makedepends after install
# --sudoloop            Loop sudo calls in the background to avoid timeout

alias cpp='pwd | xsel -b'
