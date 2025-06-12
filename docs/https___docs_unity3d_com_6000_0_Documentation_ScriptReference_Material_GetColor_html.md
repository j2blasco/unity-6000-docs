* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetColor.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetColor
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
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetColor(string name); 
## Declaration
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetColor(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Get a named color value.
Many shaders use more than one color. Use GetColor to get the `propertyName` color.  
  
Common color names used by Unity's builtin shaders:   
`"_Color"` is the main color of a material. This can also be accessed via [color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-color.html) property.   
`"_SpecColor"` is the specular color of a material (used in specular/glossy/vertexlit shaders).   
`"_EmissionColor"` is the emissive color of a material (used in vertexlit shaders).   
`"_ReflectColor"` is the reflection color of the material (used in reflective shaders).  
  
Additional resources: [color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-color.html) property, [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).
* * *
