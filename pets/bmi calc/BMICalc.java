public class BMICalc {
	
	private double h, w, result;

	public BMICalc(String height, String weight) {
		h = Double.parseDouble(height);
		w = Double.parseDouble(weight);
		result = ((w) / ((h*.01) * (h*.01)));
	}
	
	public double getCalc() {
		return result;
	}
	
}