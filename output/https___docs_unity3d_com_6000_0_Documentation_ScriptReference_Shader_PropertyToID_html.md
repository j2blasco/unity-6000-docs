* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).PropertyToID
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
## Declaration
public static int PropertyToID(string name); 
### Parameters
Parameter | Description  
---|---  
name | Shader property name.  
### Returns
**int** Unique integer for the name. 
### Description
Gets unique identifier for a shader property name.
Using property identifiers is more efficient than passing strings to all material property functions. For example if you are calling [Material.SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html) a lot, or using [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), then it is better to get the identifiers of the properties you need just once.  
  
Each name of shader property (for example, `_MainTex` or `_Color`) is assigned an unique integer number in Unity, that stays the same for the whole game. The numbers will not be the same between different runs of the game or between machines, so do not store them or send them over network.  
  
Additional resources: [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).
* * *
