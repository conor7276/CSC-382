public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        int[] arr = {1,3,4,10};
        DynamicArray array = new DynamicArray(arr);
        System.out.println("My new fancy dynamic array " + array.toString());
        array.push_back(12);
        System.out.print("Appending a new value: " + array.toString());
    }
    
}
