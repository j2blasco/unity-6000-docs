* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.ResolveMethodInfo.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).ResolveMethodInfo
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
public [Profiling.FrameDataView.MethodInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.MethodInfo.html) ResolveMethodInfo(ulong addr); 
### Parameters
Parameter | Description  
---|---  
addr | Instruction pointer.  
### Returns
**MethodInfo** Method name and location information. 
### Description
Returns method name and location information for the specified method address.
Use _ResolveMethodInfo_ to retrieve fully qualified method name of an instruction pointer in the callstack obtained with [GetItemCallstack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetItemCallstack.html).
* * *
