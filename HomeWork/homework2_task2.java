// Если необходимо, исправьте данный код:
// https://docs.google.com/document/d/17EaA1lDxzD5YigQ5OAal60fOFKVoCbEJqooB9XfhT7w/edit

public class homework2_task2 {
    public static void main(String[] args) {
        int[] intArray = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        
        if (intArray.length > 8) {
            try {
                int d = 0;
                double catchedRes1 = intArray[8] / d;
                System.out.println("catchedRes1 = " + catchedRes1);
            } catch (ArithmeticException e) {
                System.out.println("Catching exception: " + e);
            }
        } else {
            System.out.println("intArray contains less then 9 elements ");
        }
    }
}
