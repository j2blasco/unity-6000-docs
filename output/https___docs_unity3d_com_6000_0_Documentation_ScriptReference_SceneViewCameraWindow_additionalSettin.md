* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow-additionalSettingsGui.html

#  [SceneViewCameraWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.html).additionalSettingsGui
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
### Parameters
Parameter | Description  
---|---  
value | The [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) that opened the [SceneViewCameraWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.html) window.  
### Description
Subscribe to this event to receive a callback when the [SceneViewCameraWindow.OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.OnGUI.html) function is called.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[InitializeOnLoad]
static class AdditionalCameraSettings
{
    static AdditionalCameraSettings()
    {
        SceneViewCameraWindow.additionalSettingsGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow-additionalSettingsGui.html) += DoAdditionalCameraSettings;
    }  
  
    static void DoAdditionalCameraSettings(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sceneView)
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Additional Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)", EditorStyles.boldLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-boldLabel.html));  
  
        float easing = sceneView.cameraSettings.easingDuration;  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();  
  
        easing = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)("Easing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.Easing.html) Duration", easing, 0.001f, 1f);  
  
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
            sceneView.cameraSettings.easingDuration = easing;
    }
}

```

* * *
