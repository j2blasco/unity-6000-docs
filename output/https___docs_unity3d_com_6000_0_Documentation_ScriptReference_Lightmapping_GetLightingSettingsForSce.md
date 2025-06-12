* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetLightingSettingsForScene.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).GetLightingSettingsForScene
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
public static [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) GetLightingSettingsForScene([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | The [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) object.  
### Returns
**LightingSettings** The [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object if [Scene.isLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-isLoaded.html) is `true`. Otherwise returns `null`. 
### Description
Gets the [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object of a [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) object.
Additional resources: [Lightmapping.SetLightingSettingsForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingSettingsForScene.html).
* * *
