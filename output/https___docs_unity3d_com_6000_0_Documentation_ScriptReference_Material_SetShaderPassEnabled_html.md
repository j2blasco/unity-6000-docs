* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetShaderPassEnabled.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetShaderPassEnabled
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
public void SetShaderPassEnabled(string passName, bool enabled); 
### Parameters
Parameter | Description  
---|---  
passName | Shader pass name (case insensitive).  
enabled | Flag indicating whether this Shader pass should be enabled.  
### Description
Enables or disables a Shader pass on a per-Material level.
By default, all Shader passes are enabled. This function allows a Material to treat a specific Shader pass (as indicated by LightMode pass tag) as if it does not exist in the Shader. For example, if the Shader has a "refraction" pass but you only want to enable it on Materials that have a refraction Texture assigned, pass "refraction" as `passName` and false for `enabled` for Materials without a refraction Texture assigned.  
  
Additional resources: [GetShaderPassEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetShaderPassEnabled.html), RenderLoop, [Shader pass tags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html).
* * *
