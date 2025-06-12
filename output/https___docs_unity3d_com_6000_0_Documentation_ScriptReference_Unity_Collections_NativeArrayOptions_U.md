* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArrayOptions.UninitializedMemory.html

#  [NativeArrayOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArrayOptions.html).UninitializedMemory
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
Leaves [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) memory uninitialized.
Uninitialized memory can improve performance, but means that the contents of the NativeArray elements are undefined. In performance sensitive code you might use NativeArrayOptions.Uninitialized if you want to write to the entire array right after creating it without reading any of the elements first. 
* * *
