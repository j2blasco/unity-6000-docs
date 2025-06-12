* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-scenes.html

#  [EditorBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html).scenes
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
scenes; 
### Description
The list of scenes used in the active platform profile or build profile that should be inculded in the build.
When the active profile is a platform profile, this property reflects the global scenes. When the active profile is a build profile, if the build profile overrides the global scenes, it reflects the scenes specified in the build profile; otherwise, it reflects the global scenes.  
  
Note: When calling [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html) directly, [BuildPlayerOptions.scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-scenes.html) can be used instead of this property.  
  
Additional resources: [Introduction to build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html), [EditorBuildSettings.globalScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-globalScenes.html), [BuildProfile.overrideGlobalScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile-overrideGlobalScenes.html), [BuildProfile.scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile-scenes.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ExampleWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    List<SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)> m_SceneAssets = new List<SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)>();  
  
    // Add menu item named "Example Window" to the Window menu
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Example Window")]
    public static void ShowWindow()
    {
        //Show existing window instance. If one doesn't exist, make one.
        EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(ExampleWindow));
    }  
  
    void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Scenes to include in build:", EditorStyles.boldLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-boldLabel.html));
        for (int i = 0; i < m_SceneAssets.Count; ++i)
        {
            m_SceneAssets[i] = (SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html))EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(m_SceneAssets[i], typeof(SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)), false);
        }
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Add"))
        {
            m_SceneAssets.Add(null);
        }  
  
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(8);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Apply To Build Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)"))
        {
            SetEditorBuildSettingsScenes();
        }
    }  
  
    public void SetEditorBuildSettingsScenes()
    {
        // Find valid Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) paths and make a list of EditorBuildSettingsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html)
        List<EditorBuildSettingsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html)> editorBuildSettingsScenes = new List<EditorBuildSettingsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html)>();
        foreach (var sceneAsset in m_SceneAssets)
        {
            string scenePath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(sceneAsset);
            if (!string.IsNullOrEmpty(scenePath))
                editorBuildSettingsScenes.Add(new EditorBuildSettingsScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html)(scenePath, true));
        }  
  
        // Set the active platform or build profile scene list
        EditorBuildSettings.scenes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-scenes.html) = editorBuildSettingsScenes.ToArray();
    }
}

```

* * *
