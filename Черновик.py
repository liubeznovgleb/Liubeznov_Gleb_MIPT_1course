if b.hittest(target) and target.live1:
    target.hit()
    target.new_target()
    target.live1 = 0
    print("Вы попали за", count, "выстрелов")
    count = 0
if b.hittest(target) and target.live2:
    target.hit()
    target.new_target()
    target.live2 = 0
    print("Вы попали за", count, "выстрелов")
    count = 0