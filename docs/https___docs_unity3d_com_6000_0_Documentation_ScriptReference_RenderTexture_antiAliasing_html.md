* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-antiAliasing.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).antiAliasing
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
antiAliasing; 
### Description
The antialiasing level for the RenderTexture.
Anti-aliasing value indicates the number of samples per pixel. The value can be `1`, `2`, `4` or `8`. If unsupported by the hardware or rendering API, the greatest supported number of samples less than the indicated number is used.  
  
When a RenderTexture is using anti-aliasing, then any rendering into it will happen into the multi-sampled texture, which will be "resolved" into a regular texture when switching to another render target. To the rest of the system only this "resolved" surface is visible.
* * *
