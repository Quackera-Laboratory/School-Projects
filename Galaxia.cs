
//Class Decleration
class CannonLogic
{
    public int cannon_step;
    public int lazer_length;
    public int lazer_speed;
    public int lazer_width;

public CannonLogic(int cannonstep, int lazerLength, int lazerSpeed, int lazerWidth)
    {
        cannon_step = cannon_step;
        lazer_length = lazer_length;
        lazer_speed = lazer_speed;
        lazer_width = lazer_width;

    }
}
class ScoreEffects
{
        public int screen_nuke;
        public int enemy_wave;
        public int one_up;

        public int five_spread;

public ScoreEffects(int screen_nuke, int enemy_wave, int one_up, int five_spread)
    {
        screen_nuke = screen_nuke;
        enemy_wave = enemy_wave;
        one_up = one_up;
        five_spread = five_spread;

    }
}
class Powerups
{

    public int large_shot = 26;

    public int spread_shot;
    public int screen_nuke_powerup;
    public int shield;
    public int side_shot;

public Powerups(int screen_nuke, int enemy_wave, int one_up, int five_spread)
    {
        large_shot = large_shot;
        spread_shot = spread_shot;
        screen_nuke_powerup = screen_nuke_powerup;
        side_shot = side_shot;

    }
}

//spawning entities