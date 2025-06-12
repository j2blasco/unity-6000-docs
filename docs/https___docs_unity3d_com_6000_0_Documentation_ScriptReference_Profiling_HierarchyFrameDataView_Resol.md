* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ResolveItemCallstack.html

#  [HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html).ResolveItemCallstack
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
public string ResolveItemCallstack(int id); 
### Parameters
Parameter | Description  
---|---  
id | Hierarchy item identifier.  
### Returns
**string** Returns the callstack associated with the hierarchy item. Returns an empty string if the callstack is empty or if the method is unsuccessful. 
### Description
Gets the callstack associated with the specified hierarchy item.
When the callstack collection mode is enabled for certain profiler markers (such as GC.Alloc), the profiler writes the callstack to the data stream. The callstack refers to the instruction pointer stack. Instruction pointers can be resolved into function names which you can the use to identify the sample origin in the source code. _ResolveItemCallstack_ retrieves the callstack as a string. Each line represents a function call.  
  
**Note:**  
A callstack can only be resolved when profiling in the Editor. Note that a domain reload could invalidate a managed callstack. For example, when two subsequent EnterPlaymode scripts reload.  
  
Additional resources: [HierarchyFrameDataView.ResolveItemMergedSampleCallstack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ResolveItemMergedSampleCallstack.html).
* * *
