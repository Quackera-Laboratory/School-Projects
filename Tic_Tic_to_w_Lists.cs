
string[] tictacboard = {" [0] "," [1] "," [2] \n "," [3] "," [4] "," [5] \n "," [6] "," [7] "," [8] \n "};
int[,] winconditions =
{
    { 0, 1, 2 },
    { 3, 4, 5 },
    { 6, 7, 8 },
    { 0, 3, 6 },
    { 1, 4, 7 },
    { 2, 5, 8 },
    { 0, 4, 8 },
    { 2, 4, 6 }
};

static void PrintBoard(string[] tictacboard)
{
    Console.Write(tictacboard[0]);
    Console.Write(tictacboard[1]);
    Console.WriteLine(tictacboard[2]);

    Console.Write(tictacboard[3]);
    Console.Write(tictacboard[4]);
    Console.WriteLine(tictacboard[5]);

    Console.Write(tictacboard[6]);
    Console.Write(tictacboard[7]);
    Console.WriteLine(tictacboard[8]);
}
Console.WriteLine("Hello, and welcome to 3 round Tic Tac To! what is Player 1's name?");
string player1 = Console.ReadLine();
Console.WriteLine($"Great to meet you {player1}, and who is Player2?");
string player2 = Console.ReadLine();
Console.WriteLine($"Great having you as well {player2}, now lets begin!");
Console.WriteLine("You will Press the number key associated with your desired spot to play your turn");

int player1Wins = 0;
int player2Wins = 0;

string token = "X";
// still need to add player(x) choice = 0 and assighn a player(x)choice++

for (double i = 5; i > 0.5; i--)
{

token = "X";

PrintBoard(tictacboard);
Console.WriteLine("Choose a Cell\n");

string move = Console.ReadLine();
int moveNumber = int.Parse(move);

tictacboard[moveNumber] = token;
//if (CheckWin(tictacboard, token) == true)
{
    player1Wins++;
}

token = "O";

PrintBoard(tictacboard);
Console.WriteLine("Choose a Cell\n");

move = Console.ReadLine();
moveNumber = int.Parse(move);

tictacboard[moveNumber] = token;
//if (CheckWin(tictacboard, token) == true)
{
    player2Wins++;
}

};
//if (CheckWin(tictacboard, token) == false)
Console.WriteLine("Cat scratch the board?");



// cats game, declaration of winner, etc happen after the loop
//assighn a player(x)choice++
// potentially add if player(x)Wins == >=2 win call