* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Copy.html

#  [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html).Copy
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public static void Copy(NativeArray<T> src, NativeArray<T> dst); 
## Declaration
public static void Copy(T[] src, NativeArray<T> dst); 
## Declaration
public static void Copy(ReadOnly<T> src, NativeArray<T> dst); 
## Declaration
public static void Copy(NativeArray<T> src, T[] dst); 
## Declaration
public static void Copy(ReadOnly<T> src, T[] dst); 
## Declaration
public static void Copy(NativeArray<T> src, NativeArray<T> dst, int length); 
## Declaration
public static void Copy(ReadOnly<T> src, NativeArray<T> dst, int length); 
## Declaration
public static void Copy(T[] src, NativeArray<T> dst, int length); 
## Declaration
public static void Copy(NativeArray<T> src, T[] dst, int length); 
## Declaration
public static void Copy(ReadOnly<T> src, T[] dst, int length); 
## Declaration
public static void Copy(NativeArray<T> src, int srcIndex, NativeArray<T> dst, int dstIndex, int length); 
## Declaration
public static void Copy(ReadOnly<T> src, int srcIndex, T[] dst, int dstIndex, int length); 
## Declaration
public static void Copy(T[] src, int srcIndex, NativeArray<T> dst, int dstIndex, int length); 
## Declaration
public static void Copy(NativeArray<T> src, int srcIndex, T[] dst, int dstIndex, int length); 
## Declaration
public static void Copy(ReadOnly<T> src, int srcIndex, NativeArray<T> dst, int dstIndex, int length); 
### Parameters
Parameter | Description  
---|---  
src | The data to copy.  
dst | The array that receives the data.  
length | A 32-bit integer that represents the number of elements to copy. The integer must be equal to or greater than zero.  
srcIndex | A 32-bit integer that represents the index in the `src` array where copying begins.  
dstIndex | A 32-bit integer that represents the index in the `dst` array where storing begins.  
### Description
Copies a range of elements from a source array to a destination array, starting from the source index and copying them to the destination index.
* * *
