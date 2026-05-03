// public class Pain {
//     public static void main(String[] args) {
//         int[] numbers = {1, 2, 3, 4, 5};
//         int max = numbers[0];
//         for (int i = 1; i < numbers.length; i++) {
//             if (numbers[i] > max) {
//                 max = numbers[i];
//             }
//         }
//         System.out.println("The maximum number is: " + max);
//     }
// }
public class Pain {
    public static void main(String[] args) {
       String original = "Hello, World!";
         String reversed = new StringBuilder(original).reverse().toString();
            System.out.println("Original string: " + original); 
            System.out.println("Reversed string: " + reversed);
    }
}
