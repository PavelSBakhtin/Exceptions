// Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
// и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
// вместо этого, необходимо повторно запросить у пользователя ввод данных.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class homework2_task1 {
    public static void main(String[] args) {
        boolean flag = true;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while (flag) {
            System.out.print("Enter a fractional number: ");
            try {
                float fNumber = Float.parseFloat(reader.readLine());
                System.out.printf("The entered number is %f\n", fNumber);
                flag = false;
            } catch (IOException | NumberFormatException e) {
                System.out.println("Invalid input. Enter a fractional number !");
            }
        }
    }
}
