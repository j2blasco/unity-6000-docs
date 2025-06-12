* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-selectedFrameIndex.html

#  [ProfilerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html).selectedFrameIndex
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
selectedFrameIndex; 
### Description
The zero-based index of the frame currently selected in the Profiler Window.
To change the currently selected frame in the Profiler window, set this index to any value between and including [ProfilerWindow.firstAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-firstAvailableFrameIndex.html) and [ProfilerWindow.lastAvailableFrameIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow-lastAvailableFrameIndex.html). When this property is set to a value outside of that range, or smaller than 0, Unity will throw an ArgumentOutOfRangeException.  
  
If no frames are shown in the Profiler Window this index will be -1.  
  
Note: Since the Profiler Window shows the current selected frame as a 1 based index, this value will be n-1 of whatever the value the Profiler Window shows.
* * *
