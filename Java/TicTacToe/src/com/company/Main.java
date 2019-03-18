package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        String board = "|_|_|_|\n|_|_|_|\n|_|_|_|\n";
        System.out.println(board);
        Scanner reader = new Scanner(System.in);  // Reading from System.in
        System.out.println("Player 1's name: ");
        String playerName_1 = reader.nextLine(); // Scans the next token of the input as an int.
        System.out.println(playerName_1);
        System.out.println("Player 2's name: ");
        String playerName_2 = reader.nextLine(); // Scans the next token of the input as an int.
        System.out.println(playerName_2);

        char playerFlag = 'x';

        reader.close();
    }
}
