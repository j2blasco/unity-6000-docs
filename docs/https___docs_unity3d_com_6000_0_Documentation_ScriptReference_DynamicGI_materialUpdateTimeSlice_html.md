* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI-materialUpdateTimeSlice.html

#  [DynamicGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.html).materialUpdateTimeSlice
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
materialUpdateTimeSlice; 
### Description
The number of milliseconds that can be spent on material updates.
Material updates render albedo and emissive textures per system on the GPU, read them back and pass the buffers to Enlighten Realtime Global Illumination. This happens automatically for all the new systems when a scene is loaded. The timeslice amount limits how much time is spent on those steps on the main thread in each frame.  
  
Material updates are processed one system at a time until the timeslice amount is reached/exceeded. The granularity is of one system, so it is possible that material updates will take more than the timeslice amount.  
  
Minimum value: 0. If there are any scheduled material updates in the current frame, only one system will be processed.  
Maximum value: Int32.MaxValue. All the scheduled material updates will be processed in one go. Restores the pre-2017.2 behaviour.  
Default value: 8 milliseconds.
* * *
