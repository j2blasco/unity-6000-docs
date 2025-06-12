* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Release.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).Release
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
## Declaration
public void Release(); 
### Description
Releases the RenderTexture.
This function releases the hardware resources used by the render texture. The texture itself is not destroyed, and will be automatically created again when being used.  
  
As with other "native engine object" types, it is important to pay attention to the lifetime of any render textures and release them when you are finished using them, as they will not be garbage collected like normal managed types.  
  
Additional resources: [Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Create.html), [IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.IsCreated.html) functions.
* * *
