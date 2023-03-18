#include <iostream>
using namespace std;

void printArray(int* begin, int* end)
{
    for ( int* p = begin; p != end; p++ )
    {
        cout << *p << " ";
    }    
}

int insertionSort(int arr[], int n)
{
    long long step = 0;
    for ( int i = 1; i < n; i++ )
    {
        /* printArray(arr, arr+i);
        cout << "| ";
        printArray(arr+i, arr+n);
        cout << endl;*/
        
        int key = arr[i];
        int j = i-1;

        while ( j >= 0 && arr[j] > key )
        {
            arr[j+1] = arr[j];
            j--;
            step++;
        }
        arr[j+1] = key;       
    }
    return step;
}

void run( int size, int times )
{
    clock_t begin_time = clock();
    
    long long steps = 0;
    
    for ( int t = 0; t < times; t++ )
    {
        int *arr = new int[size];
    
        for ( int i = 0; i < size; i++ )
        {
            arr[i] = rand() % (size*10);        
        }
    
        //printArray(arr, arr+size);
        //cout << endl;
    
        steps += insertionSort(arr, size);

        delete[] arr;
    
        //printArray(arr, arr+size);
        //cout << endl;
    }

    clock_t end_time = clock();
    cout << size << " ";
    double nswaps = 1. * steps / times;
    printf("%.2f ", nswaps);
    
    cout << ( 1. * (end_time - begin_time) / CLOCKS_PER_SEC) << "s" << endl;
}

int main()
{
    // for ( int i = 1000; i < 10000; i += 1000 )
    //     run(i, 500);
    
    // return 0;
    run(10000,500);
}