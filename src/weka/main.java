package weka;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Archarff a= new Archarff();
		try {
			a.entrenamientio("-L 0.3 -M 0.2 -N 5 -V 0 -S 0 -E 20 -H 10");
			a.testeo();
			a.predecir();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
