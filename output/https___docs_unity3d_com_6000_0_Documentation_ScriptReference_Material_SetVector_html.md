* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetVector.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetVector
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public void SetVector(string name, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value); 
## Declaration
public void SetVector(int nameID, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_WaveAndDistance".  
value | Vector value to set.  
### Description
Sets a named vector value.
Four component vectors and colors are the same in Unity shaders. `SetVector` does almost exactly the same as [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html) just the input data type is different (`xyzw` in the vector becomes `rgba` in the color). The only difference is that color values are be converted from sRGB to Linear value, when using linear color space (see [properties in shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html)).  
  
Additional resources: [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html), [GetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetVector.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html), [Properties in Shader Programs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PropertiesInPrograms.html).
* * *
