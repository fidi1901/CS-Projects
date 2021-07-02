// Farahan Idris
// idris034
import java.util.Random;
final class Card
{

//  RANK NAME. Printable names of card ranks.

    private static final String [] rankName =
            {
                    "ace",       //   0
                    "two",       //   1
                    "three",     //   2
                    "four",      //   3
                    "five",      //   4
                    "six",       //   5
                    "seven",     //   6
                    "eight",     //   7
                    "nine",      //   8
                    "ten",       //   9
                    "jack",      //  10
                    "queen",     //  11
                    "king"       //  12
            };

//  SUIT NAME. Printable names of card suits.

    private static final String [] suitName =
            {
                    "clubs",     //  0
                    "diamonds",  //  1
                    "hearts",    //  2
                    "spades"     //  3
            };

    private int rank;  //  Rank of this CARD, between 0 and 12.
    private int suit;  //  Suit of this CARD, between 0 and 3.

//  CARD. Constructor. Make a new CARD, with a given RANK and SUIT.

    public Card(int rank, int suit)
    {
        if (0 <= rank && rank <= 12 && 0 <= suit && suit <= 3)
        {
            this.rank = rank;
            this.suit = suit;
        }
        else
        {
            throw new IllegalArgumentException("Illegal rank or suit.");
        }
    }

//  GET RANK. Return the RANK of this CARD.

    public int getRank()
    {
        return rank;
    }

//  GET SUIT. Return the SUIT of this CARD.

    public int getSuit()
    {
        return suit;
    }

//  TO STRING. Return a STRING that describes this CARD. For printing only!

    public String toString()
    {
        return rankName[rank] + " (" + rank + ") of " + suitName[suit];
    }
}

class Tableau {
    private Pile[] array = new Pile[13];
    public Tableau() {
        for (int i = 0; i <= 12; i++) {
            array[i] = new Pile();
        }
        Deck d = new Deck();
        d.shuffle();
        for (int j = 0; j < 13; j++){
            for (int i = 0; i < 4; i++){
                Card var = d.deal();
                array[j].add(var);
            }
        }
    }
    public void play(){
        boolean game = true;
        int p = 0;
        Card c1 = array[p].draw();
        System.out.println("Got " + c1.toString() + " from pile "+ p);
        while(game){
            if(array[p].isEmpty()){
                for(int i=0; i<13; i++){
                    if(!array[i].isEmpty()){
                        game = false;
                        break;
                    }
                }
                if(game){
                    System.out.println("We won!");
                    break;
                }
                else if(!game) {
                    System.out.println("Pile "+ p +" is Empty. We lost!");
                    break;
                }
            }
            Card c2 = array[p].draw();
            System.out.println("Got " + c2.toString() + " from pile "+ p);
            if(c1.getSuit() == c2.getSuit()){
                p = c1.getRank();
            }
            else{
                p = c2.getRank();
                c1 = c2;
            }
        }
    }
}





class Pile {
    private class Layer {
        private Card card;
        private Layer next;

        private Layer(Card card, Layer next) {
            this.card = card;
            this.next = next;
        }
    }

    private Layer top;

    public Pile() {
        top = null;
    }
    public void add(Card card) {
        top = new Layer(card, top);
    }
    public boolean isEmpty(){
        return top == null;
    }
    public Card draw(){
        if (isEmpty()) {
            throw new IllegalStateException();
        }
        else{
            Card d = top.card;
            top = top.next;
            return d;
        }
    }
}
class Deck {
    private Card[] deck;
    private int front = -1;
    Random r = new Random();
    private boolean dealt;

    public Deck() {
        int z = 0;
        deck = new Card[52];
        for (int i = 0; i < 13; i++) {
            for (int j = 0; j < 4; j++) {
                deck[z] = new Card(i, j);
                z++;
            }
        }
    }
    public Card deal() {
        dealt = true;
        if (front > 51) {
            throw new IllegalStateException("No more cards remain");
        }
        else{
            front ++;
            return deck[front];
        }
    }
    public void shuffle(){
        Card var;
        if (dealt){
            throw new IllegalStateException("Cards dealt already, cannot shuffle into deck");
        }
        else{
            for (int i = 51; i >= 1; i--){
                int j = Math.abs(r.nextInt()) % i;
                var = deck[j];
                deck[j] = deck[i];
                deck[i] = var;
            }
        }
    }
}
class PertedeTemps {
    public static void main(String[] args) {
        Tableau temp = new Tableau();
        temp.play();
    }
}


