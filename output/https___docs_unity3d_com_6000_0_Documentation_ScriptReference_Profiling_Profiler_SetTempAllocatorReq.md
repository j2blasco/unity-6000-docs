* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.SetTempAllocatorRequestedSize.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).SetTempAllocatorRequestedSize
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
public static bool SetTempAllocatorRequestedSize(uint size); 
### Parameters
Parameter | Description  
---|---  
size | Size in bytes.  
### Returns
**bool** Returns true if requested size was successfully set. Will return false if value is disallowed (too small). 
### Description
Sets the size of the temp allocator.
Can be used to change the size of the stack-based runtime allocator used for temporary allocations. Raise if TempAlloc.Overflow profiler markers affect runtime performance. Lower to save peak memory used.
* * *
