#!/usr/bin/env bash

theme="style_1"
dir="$HOME/.config/rofi/launchers/colorful"

ALPHA="#00000000"
BG="#1e1e2eff"
FG="#ffffffff"
SELECT="#585b70ff"
ACCENT="#f5c2e7ff"

# overwrite colors file
cat >$dir/colors.rasi <<-EOF
	/* colors */

	* {
	  al:  $ALPHA;
	  bg:  $BG;
	  se:  $SELECT;
	  fg:  $FG;
	  ac:  $ACCENT;
	}
EOF

theme="style_10"
echo $theme

rofi -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
