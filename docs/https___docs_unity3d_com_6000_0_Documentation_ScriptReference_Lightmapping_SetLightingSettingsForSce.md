* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingSettingsForScene.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).SetLightingSettingsForScene
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
public static void SetLightingSettingsForScene([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene, [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) lightingSettings); 
### Parameters
Parameter | Description  
---|---  
scene | The [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) object. If the [Scene.isLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-isLoaded.html) property is `false`, the method does not apply the settings.  
lightingSettings | The [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object.  
### Description
Applies the settings specified in the [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) object to the [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) object.
Additional resources: [Lightmapping.SetLightingSettingsForScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetLightingSettingsForScenes.html), [Lightmapping.GetLightingSettingsForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GetLightingSettingsForScene.html).
* * *
