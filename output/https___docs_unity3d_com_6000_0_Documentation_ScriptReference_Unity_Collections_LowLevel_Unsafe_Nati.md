* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility.ConvertExistingDataToNativeArray.html

#  [NativeArrayUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility.html).ConvertExistingDataToNativeArray
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
public static NativeArray<T> ConvertExistingDataToNativeArray(void* dataPointer, int length, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
dataPointer | Pointer to the preallocated data.  
length | Number of elements. The length of the data in bytes is computed automatically from this.  
allocator | The [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) type to use.  
### Returns
**NativeArray <T>** A new NativeArray, allocated with the given `allocator` strategy and wrapping the provided data. 
### Description
Converts a buffer to a NativeArray.
You can use this method to turn an existing buffer into a NativeArray. Ownership of the data is controlled via the allocation strategy that the allocator argument provides. Use [Allocator.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.None.html) if the data is owned externally, and the other arguments to transfer control to the NativeArray.
* * *
## Declaration
public static NativeArray<T> ConvertExistingDataToNativeArray(Span<T> data, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
data | Span of the preallocated data.  
allocator | The [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html)] type to use.  
### Returns
**NativeArray <T>** A new NativeArray, allocated with the given `allocator` strategy and wrapping the provided data. 
### Description
Converts a buffer to a NativeArray.
You can use this method to turn an existing buffer into a NativeArray. Ownership of the data is controlled via the allocation strategy that the allocator argument provides. Use [Allocator.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.None.html) if the data is owned externally, and the other arguments to transfer control to the NativeArray.
* * *
