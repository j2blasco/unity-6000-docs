* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1-ctor.html

# NativeArray<T0> Constructor
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
public NativeArray<T0>(T[] array, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
array | An array to copy the data from.  
allocator | The [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) to use for the data.  
### Description
Creates a NativeArray from an array of elements.
* * *
## Declaration
public NativeArray<T0>(NativeArray<T> array, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
array | The [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) to copy the data from.  
allocator | The [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) to use for the data.  
### Description
Creates a NativeArray from an existing NativeArray.
* * *
## Declaration
public NativeArray<T0>(int length, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator, [Unity.Collections.NativeArrayOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArrayOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
length | Number of elements to allocate.  
allocator | The [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) to use for the data.  
options | The [NativeArrayOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArrayOptions.html) to use for the data.  
### Description
Creates a new NativeArray and allocates enough memory to fit the provided amount of elements.
* * *
