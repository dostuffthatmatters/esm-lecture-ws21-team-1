
ffmpeg -y -framerate 2 -start_number 1 -i public/images/weekly_cycle_colored_by_month_%02d.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" public/videos/weekly_cycle_colored_by_month.gif

ffmpeg -y -framerate 2 -start_number 2010 -i public/images/concentration_over_weather_conditions_%04d.png -vf "scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" public/videos/concentration_over_weather_conditions.gif
