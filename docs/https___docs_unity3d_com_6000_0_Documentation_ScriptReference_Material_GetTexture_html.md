* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTexture.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetTexture
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
public [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) GetTexture(string name); 
## Declaration
public [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) GetTexture(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Get a named texture.
Many shaders use more than one texture. Use GetTexture to get the `propertyName` texture.  
  
If the texture is not found, the method writes an error message to the console and returns `null`.  
  
Common texture names used by Unity's builtin shaders:   
`"_MainTex"` is the main diffuse texture. This can also be accessed via [mainTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTexture.html) property.   
`"_BumpMap"` is the normal map.   
`"_Cube"` is the reflection cubemap.  
  
Additional resources: [mainTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTexture.html) property, [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).
* * *
