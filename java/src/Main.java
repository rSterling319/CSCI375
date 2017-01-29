import pastas.*;
import java.util.*;

public class Main extends Object {
	public static void main(String [] args) {
	
	
	System.out.println("Tonights menu");
	ArrayList<Pasta> pastas = new ArrayList<Pasta>();
	pastas.add(new Spagetti("MeatBalls"));
	pastas.add(new Alfredo("Shrimp"));
	pastas.add(new Alfredo());
	Spagetti spag = new Spagetti();
	System.out.println("1) " + spag.getDish());
	spag.setAddOn("Marinara");
	System.out.println("2) " + spag.getDish());
	
	int i = 3;
	
	for(Pasta pasta : pastas) {
		System.out.println(i + ") " + pasta.getDish());
		i++;	
	}
	}
}

