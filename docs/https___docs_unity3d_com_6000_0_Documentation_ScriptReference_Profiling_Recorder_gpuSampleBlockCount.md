* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder-gpuSampleBlockCount.html

#  [Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html).gpuSampleBlockCount
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
gpuSampleBlockCount; 
### Description
Gets the number of Begin/End time pairs that the GPU executed during a frame. The Recorder has a three frame delay so this gives the timings for the frame that was three frames before the one that you access this property on. (Read Only).
This represents the number of complete, or running, GPU profiling block during the frame.
* * *
