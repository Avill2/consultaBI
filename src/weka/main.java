package weka;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Archarff a= new Archarff();
		try {
			a.entrenamientio("-L 0.2 -M 0.2 -N 1500 -V 0 -S 0 -E 20 -H 4");//bueno
			//a.entrenamientio("-L 0.2 -M 0.3 -N 1500 -V 0 -S 0 -E 20 -H 2");
			//a.entrenamientio("-L 0.2 -M 0.2 -N 10000 -V 0 -S 0 -E 20 -H 4");
			//a.entrenamientio("-L 0.2 -M 0.2 -N 100 -V 0 -S 0 -E 20 -H 3");
			a.testeo();
			a.predecir();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
