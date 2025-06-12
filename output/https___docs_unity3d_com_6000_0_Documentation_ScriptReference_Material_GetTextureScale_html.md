* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTextureScale.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetTextureScale
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
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GetTextureScale(string name); 
## Declaration
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GetTextureScale(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Gets the placement scale of texture `propertyName`.
Common texture names used by Unity's builtin shaders:   
`"_MainTex"` is the main diffuse texture. This can also be accessed via [mainTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTextureScale.html) property.   
`"_BumpMap"` is the normal map.   
`"_Cube"` is the reflection cubemap.  
  
Additional resources: [mainTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTextureScale.html) property, [SetTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureScale.html).
* * *
