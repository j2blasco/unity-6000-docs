* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-maximumChunksOverride.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).maximumChunksOverride
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
maximumChunksOverride; 
### Description
Sets the limit on the number of shader variant chunks Unity loads and keeps in memory.
You can use `maximumChunksOverride` to limit the amount of memory Unity uses for [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shadervariants.html). You can use the following values: 
  * A positive value to set the maximum number of compressed shader variant chunks you want Unity to load and decompress into memory at one time.
  * `0` to load and decompress all the chunks into memory.
  * A negative value to use the value in [PlayerSettings.GetDefaultShaderChunkCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetDefaultShaderChunkCount.html).


The value only has an effect on shaders Unity has not yet loaded. If you change the value, Unity does not reload shaders in memory.  
  
Additional resources: [PlayerSettings.SetDefaultShaderChunkCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkCount.html).
* * *
