public class DynamicArray {
    private int[] arr;

    DynamicArray(int[] arr){
        this.arr = arr;
    }

    public int[] resize(){
        int size = arr.length;
        int[] resized_arr = new int[size * 2];
        // put old values back into new array
        for(int i = 0; i < size; i++){
            resized_arr[i] = arr[i];
        }
        return resized_arr;
    }
    // pushes value to the back of the array
    public int[] push_back(int value){
        // check if the array is large enough to hold another value
        
        if(arr.length <= arr.length + 1){
            arr = resize();
        }
        arr[arr.length + 1] = value;
        return arr;
    }

    public int[] insert(int value){
        
        if(arr.length < arr.length + 1 ){ // if array size cannot store new value
            arr = resize();
        }
        int[] new_arr = new int[arr.length]; 
        new_arr[0] = value; // add new value at the front
        for(int i = 1; i < arr.length; i++){ // add old values to new array
            new_arr[i] = arr[i];
        }
        return new_arr;
    }

    public int[] delete(int value){
        for (int i=0; i < arr.length; i++){ // look for value to delete
            if(arr[i] == value){ // if value is found keep track of where it is
                int del = i;
                int[] new_arr = new int[arr.length];
                for(int j = 0; j < arr.length; j++){ // don't add new value to new array
                    if(j == i){
                        continue;
                    }
                    new_arr[i] = arr[i];
                }
                return new_arr;
            }
        }

        return arr;
    }

    public int[] getArray(){
        return arr;
    }

    public String toString(){
        System.out.print("Printing out array: ");
        String s = "";
        for(int num = 0; num < arr.length; num++){
            System.out.print(arr[num] + " ");
        }
        return s;
    }
}
