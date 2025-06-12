* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-dilatedRange.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).dilatedRange
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
dilatedRange; 
### Description
The [Light.range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-range.html) property describes the range of each point on the light. However, area lights consist of several light-emitting points, and so the effective range is a bit larger, and depends on the size of the area light. This property returns this larger range. Use this property to find whether a given world-space point will be lit by the area light.  
  
If not an area light, then returns the same value as Light.range. 
* * *
