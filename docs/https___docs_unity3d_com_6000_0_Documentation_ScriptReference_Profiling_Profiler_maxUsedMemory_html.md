* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-maxUsedMemory.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).maxUsedMemory
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
maxUsedMemory; 
### Description
Sets the maximum amount of memory that Profiler uses for buffering data. This property is expressed in bytes.
When Profiler is enabled, it collects data continuously and either saves the data to a file or sends it to the Editor.  
  
Depending on disk write speed or network bandwidth, Profiler may collect more data than it is able to write. If this happens, Profiler accumulates data in a ring buffer chain and stops collecting data when the total size of the buffer chain reaches the _maxUsedMemory_ limit. Profiler data collection resumes when it is able to write data.  
  
By default, _maxUsedMemory_ is 128MB for Players and 512MB for the Editor. You can use the **-profiler-maxusedmemory** command line argument to set the _maxUsedMemory_ parameter at startup. For example, _-profiler-maxusedmemory 16777216_ ,  
  
Additional resources: [Profiler.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html).
* * *
