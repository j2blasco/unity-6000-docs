* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeDisableParallelForRestrictionAttribute.html

# NativeDisableParallelForRestrictionAttribute
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
Indicates that multiple jobs can safely access the same NativeContainer at the same time.
Usually it's unsafe for multiple jobs to access the same NativeContainer at the same time. This attribute makes it safe to do so, and is a required attribute for [wiki:JobSystemParallelForJobs|parallel jobs]]. A parallel job needs this attribute because you must define how to safely access a native container yourself, and `NativeDisableParallelForRestriction` lets you ignore multiple reads and writes to a container.
* * *
