* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.AccessViolation.html

#  [ForcedCrashCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.html).AccessViolation
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
Cause a crash by performing an invalid memory access.  
  
The invalid memory access is performed on each platform as follows:
**OSX, Android** : Invoked using **raise(SIGSEGV)** ;  
  
**Windows, Windows Store** : Invoked using **RaiseException** with EXCEPTION_ACCESS_VIOLATION  
  
**Other** : Invoked using **int* p = NULL; *p = 5;**
* * *
