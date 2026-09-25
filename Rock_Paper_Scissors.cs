int player1Wins = 0;
int player2Wins = 0;

Console.WriteLine("  \n Hello, \n \t Welcome, \n \t \t Legendary Challengers!!!");
Console.WriteLine("Player 1, please tell us your name?");
string player1 = Console.ReadLine();
Console.WriteLine("Player 2, please tell us your name?");
string player2 = Console.ReadLine();
Console.WriteLine($"Welcome, {player1} and {player2}, May the true dragon warrior succeed in the sacred match count.");
// around This will be the start of a 3 round loop
Console.WriteLine("\n \n Choose your Weapons!!!");

string player1Choice = Console.ReadLine();

if (player1Choice == "rock" || player1Choice == "Rock" || player1Choice == "r" || player1Choice == "R") 
{ Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}
if (player1Choice == "paper" || player1Choice == "Paper" || player1Choice == "p" || player1Choice == "P") 
{
    Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}
if (player1Choice == "scissors" || player1Choice == "Scissors" || player1Choice == "s" || player1Choice == "S") 
{
    Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}
Console.WriteLine("A true warriors selection. May we have another?");
string player2Choice = Console.ReadLine();

if (player2Choice == "rock" || player2Choice == "Rock" || player2Choice == "r" || player2Choice == "R") 
{
    Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}
if (player2Choice == "paper" || player2Choice == "Paper" || player2Choice == "p" || player2Choice == "P") 
{
    Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}
if (player2Choice == "scissors" || player2Choice == "Scissors" || player2Choice == "s" || player2Choice == "S") 
{
    Console.WriteLine("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    }

// compare all 9 possible game states

if ((player1Choice == "rock" || player1Choice == "Rock" || player1Choice == "r" || player1Choice == "R") && (player2Choice == "rock" || player2Choice == "Rock" || player2Choice == "r" || player2Choice == "R"))
{
    Console.WriteLine("\n Two immortal dragons clash forever");
}
if ((player1Choice == "rock" || player1Choice == "Rock" || player1Choice == "r" || player1Choice == "R") && (player2Choice == "paper" || player2Choice == "Paper" || player2Choice == "p" || player2Choice == "P"))
{
    Console.WriteLine("\n The rock crushed and pasted into a beautiful dress for the paper");
    player2Wins++;
}
if ((player1Choice == "rock" || player1Choice == "Rock" || player1Choice == "r" || player1Choice == "R") && (player2Choice == "scissors" || player2Choice == "Scissors" || player2Choice == "s" || player2Choice == "S"))
{
    Console.WriteLine("\n The puny scissors clatter as seperated blades");
    player1Wins++;
}
if ((player1Choice == "paper" || player1Choice == "Paper" || player1Choice == "p" || player1Choice == "P") && (player2Choice == "paper" || player2Choice == "Paper" || player2Choice == "p" || player2Choice == "P"))
{
    Console.WriteLine("\n Good luck cheating off each other now");
}
if ((player1Choice == "paper" || player1Choice == "Paper" || player1Choice == "p" || player1Choice == "P") && (player2Choice == "rock" || player2Choice == "Rock" || player2Choice == "r" || player2Choice == "R"))
{
    Console.WriteLine("\n Poor Rock turned sedimantary");
    player1Wins++;
}
if ((player1Choice == "paper" || player1Choice == "Paper" || player1Choice == "p" || player1Choice == "P") && (player2Choice == "scissors" || player2Choice == "Scissors" || player2Choice == "s" || player2Choice == "S"))
{
    Console.WriteLine("\n The paper made for a beautiful snow");
    player2Wins++;
}
if ((player1Choice == "scissors" || player1Choice == "Scissors" || player1Choice == "s" || player1Choice == "S") && (player2Choice == "paper" || player2Choice == "Paper" || player2Choice == "p" || player2Choice == "P"))
{
    Console.WriteLine("\nTo Shreds you say?.");
    player1Wins++;
}
if ((player1Choice == "scissors" || player1Choice == "Scissors" || player1Choice == "s" || player1Choice == "S") && (player2Choice == "scissors" || player2Choice == "Scissors" || player2Choice == "s" || player2Choice == "S"))
{
    Console.WriteLine("\n the blades unsure of their absolute value each left.");
}
if ((player1Choice == "scissors" || player1Choice == "Scissors" || player1Choice == "s" || player1Choice == "S") && (player2Choice == "rock" || player2Choice == "Rock" || player2Choice == "r" || player2Choice == "R"))
{
    Console.WriteLine("Hard Rock crushes thin steel");
    player2Wins++;
}

Console.WriteLine("\n \n \t The sacred match count has been reached");
if (player1Wins > player2Wins)
{
    Console.WriteLine($"{player1} Has Proven themself the Dragon Warrior!");
}
if (player2Wins > player1Wins)
{
    Console.WriteLine($"{player2} Has Proven themself the Dragon Warrior!");
}
if (player1Wins == player2Wins)
{
    Console.WriteLine("The Dragon Warrior has not yet been chosen, the battle continues eternally!");
}