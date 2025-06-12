* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeSlice_1-ctor.html

# NativeSlice<T0> Constructor
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
public NativeSlice<T0>(NativeArray<T> array); 
## Declaration
public NativeSlice<T0>(NativeArray<T> array, int start); 
## Declaration
public NativeSlice<T0>(NativeArray<T> array, int start, int length); 
## Declaration
public NativeSlice<T0>(NativeSlice<T> slice, int start); 
## Declaration
public NativeSlice<T0>(NativeSlice<T> slice, int start, int length); 
### Parameters
Parameter | Description  
---|---  
array | The [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) to use.  
slice | The [NativeSlice<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeSlice_1.html) to use.  
start | The start index in the NativeArray or NativeSlice.  
length | The number of elements that the new NativeSlice will have.  
### Description
Constructs a new NativeSlice from a NativeArray or NativeSlice.
* * *
