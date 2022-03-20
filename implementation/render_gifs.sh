ffmpeg -framerate 2.5 -start_number 2010 -i renders/weekly_cycle_%04d.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" renders/weekly_cycle_by_year.gif

ffmpeg -framerate 2.5 -start_number 1 -i renders/weekly_cycle_%02d.2016.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" renders/weekly_cycle_2016_by_month.gif

ffmpeg -framerate 2.5 -start_number 1 -i renders/weekly_cycle_%02d.2017.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" renders/weekly_cycle_2017_by_month.gif

ffmpeg -framerate 2.5 -start_number 1 -i renders/weekly_cycle_%02d.2018.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" renders/weekly_cycle_2018_by_month.gif

ffmpeg -framerate 2.5 -start_number 1 -i renders/weekly_cycle_%02d.2019.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" renders/weekly_cycle_2019_by_month.gif