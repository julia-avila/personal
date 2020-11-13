import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;

public class BMICalcGUI {
	
	
	private JFrame frame;
	private Container cont;
	private JPanel left, right;
	private JLabel height, weight, head, result, status;
	private TextField entHeight, entWeight;
	private JButton calc;
	private BMICalc obj;
	private double input;
	
	public BMICalcGUI() {
		
		frame = new JFrame();
		cont = new Container();
		left = new JPanel();
		right = new JPanel();
		
		height = new JLabel("Height in cm:");
		weight = new JLabel("Weight in kg:");
		
		entHeight = new TextField();
		entWeight = new TextField();
		head = new JLabel("Your BMI is:");
		result = new JLabel();
		status = new JLabel();
		
		calc = new JButton("Calculate");
	}
	
	public void setUpGUI() {
		frame.setSize(240, 140);
		frame.setTitle("BMI Calculator");
		
		cont = frame.getContentPane();
		cont.setLayout(new GridLayout(1,2));
		
		cont.add(left);
		cont.add(right);
		
		right.setLayout(new GridLayout(3,1));
		
		left.add(height);
		left.add(entHeight);
		left.add(weight);
		left.add(entWeight);
		left.add(calc);
		right.add(head);
		right.add(result);
		right.add(status);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
		
	}
	
	public void setUpButtonListeners() {
		ActionListener calculate = new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ae) {
				obj = new BMICalc(entHeight.getText(), entWeight.getText());
				double res = obj.getCalc();
				//String res = String.valueOf(obj.getCalc());
				if (obj.getCalc() <  18.5) {
					result.setText(String.format("%.2f", res));
					status.setText("UNDERWEIGHT");
					status.setForeground(new Color(255,0,0));
				} else if ((obj.getCalc() > 18.4) && (obj.getCalc() < 25.0)) {
					result.setText(String.format("%.2f", res));
					status.setText("NORMAL");
					status.setForeground(new Color(0,128,0));
				} else if ((obj.getCalc() > 24.9) && (obj.getCalc() < 30.0)) {
					result.setText(String.format("%.2f", res));
					status.setText("OVERWEIGHT");
					status.setForeground(new Color(255,165,0));
				} else {
					result.setText(String.format("%.2f", res));
					status.setText("OBESE");
					status.setForeground(new Color(255,0,0));
				}
			}
		};
		
		
		calc.addActionListener(calculate);
	}

}