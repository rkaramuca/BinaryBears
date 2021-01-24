import java.util.Scanner;

class prob3 {
	public static void main(String[] args) {
		// get number of test cases and open Scanner
		Scanner in = new Scanner(System.in);
		int cases = Integer.parseInt(in.nextLine());
		for(int i = 0; i < cases; i++) {
			// get each test case one-by-one
			String curr = in.nextLine();
			
			// break it into pieces
			String hat[] = curr.split(" ");
			String model = hat[1];
			String mat = hat[2];
			Double size = Double.parseDouble(hat[3]);
			String frac;
			// if there is a 5th piece (fraction to size),
			// get the fraction quotient and add it to the size
			if(hat.length == 5) {
				frac = hat[4];		
				String f[] = frac.split("/");
				size += Double.parseDouble(f[0]) / Double.parseDouble(f[1]);
			}
			
			// calc the circumference, radius, and areas for 
			// each piece of the hat
			double cir = (25/8) * size;
			double r = cir / (2 * 3.14159);
			double top = 3.14159 * (Math.pow(r, 2));
			double mid = 2 * 3.14159 * r * 4;
			double brim = (3.14159 * (Math.pow((r + 3), 2))) - (3.14159 * (Math.pow(r, 2)));

			// calculate overall area, find material cost, then calc total cost
			double area = top + mid + brim;
			double matC = 0;
			if(mat.equals("velvet"))
				matC = .25;
			else if(mat.equals("straw"))
				matC = .35;
			else if(mat.equals("wool"))
				matC = .45;
			double cost = area * matC;
			
			// round string then print
			String c = String.format("%.2f", cost);
			String out = "Model " + model + " $ " + c; 
			System.out.println(out);
		}
	}
}
