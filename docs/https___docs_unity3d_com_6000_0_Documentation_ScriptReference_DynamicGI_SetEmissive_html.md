* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.SetEmissive.html

#  [DynamicGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.html).SetEmissive
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
public static void SetEmissive([Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color); 
### Parameters
Parameter | Description  
---|---  
renderer | The [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) that should get a new color.  
color | The emissive [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).  
### Description
Allows to set an emissive color for a given renderer quickly, without the need to render the emissive input for the entire system.
Note that a subsequent [DynamicGI.UpdateMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.UpdateMaterials.html) call on _any_ renderer within the system will clear the effects of DynamicGI.SetEmissive.  
  
Additional resources: [UpdateMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.UpdateMaterials.html).
* * *
