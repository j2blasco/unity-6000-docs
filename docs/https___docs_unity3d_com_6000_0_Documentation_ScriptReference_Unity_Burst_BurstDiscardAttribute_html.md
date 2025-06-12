* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Burst.BurstDiscardAttribute.html

# BurstDiscardAttribute
class in Unity.Burst
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
Use this attribute to exclude a method or property from being compiled to native code by the Burst compiler.
By default, Burst compiles all methods in jobs decorated with the `[BurstCompile]` attribute. You can use the `[BurstDiscard]` attribute on a method or property to exclude code from Burst compilation in situations where it can only run in .NET runtimes. For example, you can use `[BurstDiscard]` to exclude methods that use managed objects to perform logging, or methods that check the validity of something only valid in a managed environment.
```
using Unity.Burst;
using Unity.Collections;
using Unity.Jobs;
using UnityEngine;  
  
[BurstCompile]
public struct MyJob : IJob[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJob.html)
{
    // ...  
  
    [BurstDiscard]
    public void NotExecutedInNative()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This is a log from a managed job");
    }  
  
    public void Execute()
    {
        // The following method call will not be compiled
        NotExecutedInNative();
    }
}

```

* * *
