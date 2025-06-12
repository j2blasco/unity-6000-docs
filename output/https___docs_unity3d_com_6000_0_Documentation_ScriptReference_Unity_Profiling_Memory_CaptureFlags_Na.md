* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeStackTraces.html

#  [CaptureFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.html).NativeStackTraces
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
Specifies that Call-Stack Symbols for the Native Call-stack of each Allocation should be collected.
Native Call stacks can only be collected from a build that supports the collection of Native Call-stack information, which currently requires Source Code access. To be able to connect each allocation to its Call-stack, the [CaptureFlags.NativeAllocationSites](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html) needs to be specified as well.  
  
Corresponds to the NativeCallstackSymbol field in a Memory Snapshot.
* * *
