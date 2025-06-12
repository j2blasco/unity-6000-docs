* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.html

# ReadOnly
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
Represents a [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) interface constrained to read-only operations.
### Properties
Property | Description  
---|---  
[IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.IsCreated.html) | Indicates that a ReadOnly has an allocated memory buffer.  
[Length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.Length.html) | Provides the number of elements in the ReadOnly.  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.Index_operator.html) | Provides read-only access to ReadOnly elements by index.  
### Public Methods
Method | Description  
---|---  
[AsReadOnlySpan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.AsReadOnlySpan.html) | Exposes ReadOnly data as a System.ReadOnlySpan<T>.  
[CopyTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.CopyTo.html) | Copies all elements to a ReadOnly or managed array of the same length.  
[GetEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.GetEnumerator.html) | Gets an enumerator.  
[Reinterpret](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.Reinterpret.html) | Reinterpret a ReadOnly with a different data type (type punning).  
[ToArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.ToArray.html) | Convert the data in a ReadOnly to a managed array.  
[UnsafeElementAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.ReadOnly.UnsafeElementAt.html) | Provides read-only access to ReadOnly elements by index.  
* * *
