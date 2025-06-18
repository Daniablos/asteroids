def handle_collisions(player, asteroids, shots):
    for a in asteroids:
        for s in shots:
            if s.collision(a):
                a.split()
                s.kill()
        if a.collision(player):
            raise SystemExit("Game over!")
