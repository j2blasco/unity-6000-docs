* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.WrappedAround.html

#  [ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html).WrappedAround
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
WrappedAround; 
### Description
Indicates if ProfilerRecorder capacity has been exceeded.
Returns true if ProfilerRecorder capacity has been exceeded and WrapAroundWhenCapacityReached had been specified.  
  
If ProfilerRecorder is created with [ProfilerRecorderOptions.WrapAroundWhenCapacityReached](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderOptions.WrapAroundWhenCapacityReached.html) the Count property determines the index of the next sample to be collected. You can look at it as a running index in a round-robin sample buffer. This is useful in use cases such as mapping data to the histogram texture.
* * *
