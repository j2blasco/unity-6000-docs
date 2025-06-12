* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.DeallocateOnJobCompletionAttribute.html

# DeallocateOnJobCompletionAttribute
class in Unity.Collections
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
Automatically deallocates a native container when a job is finished.
Use this attribute on native container fields marked with [NativeContainerSupportsDeallocateOnJobCompletionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsDeallocateOnJobCompletionAttribute.html) in a job struct. In particular, fields of type NativeArray can be automatically deallocated with this attribute. When the job finishes execution, the job system automatically deallocates the native container.  
  
Additional resources: [NativeContainerSupportsDeallocateOnJobCompletionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsDeallocateOnJobCompletionAttribute.html)
* * *
