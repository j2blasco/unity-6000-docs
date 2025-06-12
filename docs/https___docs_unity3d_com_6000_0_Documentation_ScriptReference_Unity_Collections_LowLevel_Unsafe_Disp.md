* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.DisposeSentinel.Clear.html

#  [DisposeSentinel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.DisposeSentinel.html).Clear
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
public static void Clear(ref [Unity.Collections.LowLevel.Unsafe.DisposeSentinel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.DisposeSentinel.html) sentinel); 
### Parameters
Parameter | Description  
---|---  
sentinel | The `DisposeSentinel` to clear.  
### Description
Clears the `DisposeSentinel`.
A `DisposeSentinel` is usually cleared when the related `NativeContainer` is disposed.
* * *
