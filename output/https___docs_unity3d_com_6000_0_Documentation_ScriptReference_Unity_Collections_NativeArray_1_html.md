* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html

# NativeArray<T0>
struct in Unity.Collections
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Provides a buffer of native memory to managed code, making it possible to share data between managed and native code without marshalling costs.
A NativeArray instance provides systems that means you can use them safely in jobs. A NativeArray also has automatic memory leak tracking.
### Properties
Property | Description  
---|---  
[IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.IsCreated.html) | Indicates that a NativeArray<T0> has an allocated memory buffer.  
[Length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Length.html) | Number of elements in a NativeArray<T0>.  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Index_operator.html) | Access NativeArray<T0> elements by index.  
### Constructors
Constructor | Description  
---|---  
[NativeArray_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1-ctor.html) | Creates a NativeArray from an array of elements.  
### Public Methods
Method | Description  
---|---  
[AsReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.AsReadOnly.html) | Casts a NativeArray<T0> to read-only array.  
[AsReadOnlySpan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.AsReadOnlySpan.html) | Exposes NativeArray<T0> data as a System.ReadOnlySpan<T>.  
[AsSpan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.AsSpan.html) | Exposes NativeArray<T0> data as a System.Span<T>.  
[CopyFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.CopyFrom.html) | Copies all the elements from a NativeArray<T0> or a managed array of the same length.  
[CopyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.CopyTo.html) | Copies all the elements to another NativeArray<T0> or a managed array of the same length.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Dispose.html) | Disposes a NativeArray<T0>.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Equals.html) | Compares two NativeArray<T0> instances.  
[GetEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.GetEnumerator.html) | Gets an enumerator.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.GetHashCode.html) | Gets a hash code for the current instance.  
[GetSubArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.GetSubArray.html) | Gets a view into an array starting at the specified index.  
[Reinterpret](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Reinterpret.html) | Reinterpret a NativeArray<T0> with a different data type (type punning).  
[ReinterpretLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReinterpretLoad.html) | Reinterpret and load data starting at underlying index as a different type.  
[ReinterpretStore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReinterpretStore.html) | Reinterpret and store data starting at underlying index as a different type.  
[ToArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ToArray.html) | Convert a NativeArray<T0> to an array.  
### Static Methods
Method | Description  
---|---  
[Copy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.Copy.html) | Copies a range of elements from a source array to a destination array, starting from the source index and copying them to the destination index.  
* * *
