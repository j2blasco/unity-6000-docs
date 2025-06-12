* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.RenderProbe.html

#  [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).RenderProbe
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html "Go to ReflectionProbe Component in the Manual")
## Declaration
public int RenderProbe([RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) targetTexture = null); 
### Parameters
Parameter | Description  
---|---  
targetTexture | Target RenderTexture in which rendering should be done. Specifying null will update the probe's default texture.  
### Returns
**int** An integer representing a RenderID which can subsequently be used to check if the probe has finished rendering while rendering in time-slice mode.  
  
Additional resources: [IsFinishedRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.IsFinishedRendering.html) Additional resources: [timeSlicingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe-timeSlicingMode.html)
### Description
Refreshes the probe's cubemap.
* * *
