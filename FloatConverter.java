import java.util.Scanner;

public class FloatConverter {
    private char output_sign = '0';
    private String output_expo = "";
    private String output_mantissa = "";
    private String output_raw;

    public void IEEE(float input) {
        int bits = Float.floatToIntBits(input);
        this.output_raw = Integer.toBinaryString(bits);
        if (this.output_raw.length() == 32) {
            this.output_sign = this.output_raw.charAt(0);
            for (int i = 1; i < 32; i++) {
                if (i < 9) {
                    this.output_expo += Character.toString(this.output_raw.charAt(i));
                } else {
                    this.output_mantissa += Character.toString(this.output_raw.charAt(i));
                }
            }
        } else {
            for (int i = 0; i < 31; i++) {
                if (i < 8) {
                    this.output_expo += Character.toString(this.output_raw.charAt(i));
                } else {
                    this.output_mantissa += Character.toString(this.output_raw.charAt(i));
                }
            }
            this.output_raw = this.output_sign + this.output_raw;
        }
    }

    public static void main(String[] args) {
        FloatConverter FloatConverter = new FloatConverter();
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Input real number: ");
        float input = keyboard.nextFloat();
        keyboard.close();
        FloatConverter.IEEE(input);
        System.out.printf("Output1 sign: %c %n", FloatConverter.output_sign);
        System.out.printf("Output2 expo: %s %n", FloatConverter.output_expo);
        System.out.printf("Output3 mantissa: %s %n", FloatConverter.output_mantissa);
        System.out.printf("Output RAW: %s", FloatConverter.output_raw);
    }
}