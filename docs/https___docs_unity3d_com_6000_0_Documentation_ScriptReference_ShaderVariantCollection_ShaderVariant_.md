* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.ShaderVariant.html

# ShaderVariant
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Identifies a specific variant of a shader.
In Unity, many shaders internally have multiple "variants", to account for different light modes, lightmaps, shadows and so on. These variants are indentified by a shader pass type, and a set of shader keywords. See [ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html).  
  
Note that creating a ShaderVariant will throw an ArgumentException if shader is null, pass type does not exist or variant with the passed keywords is not found.
### Properties
Property | Description  
---|---  
[keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.ShaderVariant-keywords.html) | Array of shader keywords to use in this variant.  
[passType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.ShaderVariant-passType.html) | Pass type to use in this variant.  
[shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.ShaderVariant-shader.html) | Shader to use in this variant.  
### Constructors
Constructor | Description  
---|---  
[ShaderVariantCollection.ShaderVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.ShaderVariant-ctor.html) | Creates a ShaderVariant structure.  
* * *
