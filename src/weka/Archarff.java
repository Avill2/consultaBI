package weka;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.evaluation.Prediction;
import weka.classifiers.functions.MultilayerPerceptron;
import weka.classifiers.misc.SerializedClassifier;
import weka.core.Debug;
import weka.core.Instances;
import weka.core.Utils;

public class Archarff {
	
	
	
	public void entrenamientio(String paramsNN) {
		
		System.out.println(paramsNN);
		
		try {
			
			//FileReader trainreader =new FileReader("src/weka/entrenamiento.arff");
			FileReader trainreader =new FileReader("src/weka/dataQuito.arff");
			
			//instancias
			Instances train= new Instances(trainreader);
			train.setClassIndex(train.numAttributes()-1);
			
			
			//red nueronal
			MultilayerPerceptron mlp=new MultilayerPerceptron();
			mlp.setOptions(Utils.splitOptions(paramsNN));
			mlp.buildClassifier(train);
			
			
			Debug.saveToFile("src/red/RedNeuronalEntrenada.train", mlp);
			
			//evaluar el entranamiento
			Evaluation evaluarTrain = new Evaluation(train);
			evaluarTrain.evaluateModel(mlp,  train);
			System.out.println(evaluarTrain.toSummaryString("Resumen",false));
			System.out.println(evaluarTrain.toMatrixString("Matrix con."));
			
			
			trainreader.close();
			
			
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("algo fue mal en el entrenamiento");
		}
	}
	
	public void testeo(){
try {
			
			FileReader testreader =new FileReader("src/weka/test.arff");
			
			//instancias
			Instances test= new Instances(testreader);
			test.setClassIndex(test.numAttributes()-1);
			
			Evaluation evaluaTest= new Evaluation(test);
			SerializedClassifier clasificador=new SerializedClassifier();
			clasificador.setModelFile(new File("src/red/RedNeuronalEntrenada.train"));
			Classifier alp=clasificador.getCurrentModel();
			
			evaluaTest.evaluateModel(alp, test);
			System.out.println(evaluaTest.toSummaryString("Resumen", false));
            System.out.println(evaluaTest.toMatrixString("Matrix Con."));

			
			
			testreader.close();
			
			
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("algo fue mal en el testeo");
		}
	}
	
	public void predecir(){
try {
			
			//FileReader testreader =new FileReader("src/weka/prediccion.arff");
	//FileReader testreader =new FileReader("src/weka/dataCuenca.arff");
	//FileReader testreader =new FileReader("src/weka/dataQuito.arff");
	FileReader testreader =new FileReader("src/weka/dataGuayaquil.arff");
			
			//instancias
			Instances test= new Instances(testreader);
			//todos los atributos menos el resultado
			test.setClassIndex(test.numAttributes()-1);
			
			SerializedClassifier classifier=new SerializedClassifier();
			Evaluation evaltest= new Evaluation(test);
			classifier.setModelFile(new File("src/red/RedNeuronalEntrenada.train"));
			
			Classifier mlp= classifier.getCurrentModel();
			evaltest.evaluateModel(mlp,test);
			ArrayList <Prediction> precciones =evaltest.predictions();
			
			int sis=0,nos=0;
			for(int i=0;i<precciones.size();i++){
				Prediction p= precciones.get(i);
				
				if (p.predicted()==1) {
					sis++;
				}else {
					nos++;
				}
				System.out.println(p.predicted());
			}
			
			System.out.println("Sis: "+sis+" ,NOs: "+nos);
			
			
			
			
			testreader.close();
			
			
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("algo mal prediciendo mal");
		}
	}
	
	public String predecir(String datos){
		String resultado="";
		try {
			String ruta = "src/weka/unico.arff";
			File archivo = new File(ruta);
			BufferedWriter bw;
			if(archivo.exists()) {
				bw = new BufferedWriter(new FileWriter(archivo));			
			} else {
				bw = new BufferedWriter(new FileWriter(archivo));
			}
			bw.write("@relation ConsolidatedTrainData"
			+ "\n@attribute tendtexto numeric"
				    + "\n@attribute tendhashtag numeric"
				    + "\n@attribute retweeted numeric"
				    + "\n@attribute favourited numeric"
				    + "\n@attribute tendencia numeric"
				    + "\n@data");
			bw.write(datos+","+"?");
			bw.close();


			//PREDICIENDO
			FileReader testreader =new FileReader("src/weka/unico.arff");

			//instancias
			Instances test= new Instances(testreader);
			test.setClassIndex(test.numAttributes()-1);

			SerializedClassifier classifier=new SerializedClassifier();
			Evaluation evaltest= new Evaluation(test);
			classifier.setModelFile(new File("src/weka/RedNeuronalEntrenada.train"));

			Classifier mlp= classifier.getCurrentModel();
			evaltest.evaluateModel(mlp,test);
			ArrayList <Prediction> precciones =evaltest.predictions();

			for(int i=0;i<precciones.size();i++){
				Prediction p= precciones.get(i);
				resultado=String.valueOf(p.predicted()+"");
				//System.out.println(p.predicted());
			}




			testreader.close();


		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("mal");
		}
		

		if(resultado.contains("1")){
			resultado="Tendencia por el SI";
			
		}else
			resultado="Tendencia por el NO";
			


		return resultado;
	}


}
