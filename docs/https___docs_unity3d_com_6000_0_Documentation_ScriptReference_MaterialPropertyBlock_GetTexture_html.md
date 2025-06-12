* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.GetTexture.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).GetTexture
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
Get a texture from the property block.
Returns null if not found.
* * *
