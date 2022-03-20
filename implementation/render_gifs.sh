ffmpeg -framerate 2.5 -start_number 2010 -i renders/weekly_cycle_%04d.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" renders/weekly_cycle.gif
