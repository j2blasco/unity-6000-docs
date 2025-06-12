* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.html

# ForcedCrashCategory
enumeration
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
Specifies the category of crash to cause when calling ForceCrash().
### Properties
Property | Description  
---|---  
[AccessViolation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.AccessViolation.html) | Cause a crash by performing an invalid memory access.The invalid memory access is performed on each platform as follows:  
[FatalError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.FatalError.html) | Cause a crash using Unity's native fatal error implementation.  
[Abort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.Abort.html) | Cause a crash by calling the abort() function.  
[PureVirtualFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.PureVirtualFunction.html) | Cause a crash by calling a pure virtual function to raise an exception.  
[MonoAbort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.MonoAbort.html) | Cause a crash by calling the abort() function within the Mono dynamic library.  
* * *
