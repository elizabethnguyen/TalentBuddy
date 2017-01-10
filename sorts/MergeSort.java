import java.util.*;

public class MergeSort
{
	public static void main(String args[])
	{
		int[] data = {3, 1, 2, 4, 9, 3};
		System.out.println("Start: " + Arrays.toString(data));
		mergeSort(data);
		System.out.println("End: " + Arrays.toString(data));
	}

	public static void mergeSort(int[] data)
	{
		mergeSort(data, 0, data.length-1);
	}

	public static void mergeSort(int[] data, int leftIdx, int rightIdx)
	{
		if (leftIdx < rightIdx) {
			int middleIdx = (rightIdx - leftIdx) / 2 + leftIdx;
			mergeSort(data, leftIdx, middleIdx);
			mergeSort(data, middleIdx+1, rightIdx);
			merge(data, leftIdx, middleIdx, rightIdx);
		}
	}

	public static void merge(int[] data, int leftIdx, int middleIdx, int rightIdx)
	{
		int[] leftArray = new int[middleIdx-leftIdx+1];
		int[] rightArray = new int[rightIdx-middleIdx];

		int i = 0; // pointer for the left array
		int j = 0; // pointer for the right array

		int k = leftIdx;

		// copy values from data array to respective left and right
		for (i = leftIdx; i <= middleIdx; i++) {
			leftArray[j] = data[i];
			j++;
		}

		j = 0;
		
		for (i = middleIdx+1; i <= rightIdx; i++) {
			rightArray[j] = data[i];
			j++;
		}

		// the real sort
		i = 0;
		j = 0;

		while (i < leftArray.length && j < rightArray.length)
		{
			if (leftArray[i] < rightArray[j]) {
				data[k] = leftArray[i];
				i++;
			} else {
				data[k] = rightArray[j];
				j++;
			}
			k++;
		}
			
		// empty out the remaining array that still has elements (i or j have not reached the end of their respective array)
		for (; i < leftArray.length; i++) {
			data[k] = leftArray[i];
			k++;
		}

		for (; j < rightArray.length; j++) {
			data[k] = rightArray[j];
			k++;
		}

	}
}
