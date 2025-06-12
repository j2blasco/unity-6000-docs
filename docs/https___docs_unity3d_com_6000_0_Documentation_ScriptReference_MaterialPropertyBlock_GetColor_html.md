* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.GetColor.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).GetColor
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
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetColor(string name); 
## Declaration
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetColor(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Get a color from the property block.
Returns (0, 0, 0, 0) if not found. If the value is previously set using [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetColor.html), the returned value is converted from the currently active color space back to the sRGB color space.  
  
Additional resources: [GetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.GetVector.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetVector.html), [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetColor.html).
* * *
