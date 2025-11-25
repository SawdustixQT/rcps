local player = {x = 400, y = 300, size = 40, speed = 20, color = {100, 255, 100}}

function init()
    print("game init")
end

function key_press(key)
    if key == "Left" then
        player.x = player.x - player.speed
    elseif key == "Right" then
        player.x = player.x + player.speed
    elseif key == "Up" then
        player.y = player.y - player.speed
    else
        player.y = player.y + player.speed
    end
end

function update()
   
end

function draw()
    clear(30, 30, 60)  -- Тёмно-синий фон
    -- Рисуем три разноцветных квадрата
    rect(player.x - player.size / 2, player.y - player.size / 2, player.size, player.size, player.color[1], player.color[2], player.color[3])
   
end
