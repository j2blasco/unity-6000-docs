* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneManagerSetupRestored.html

#  [EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html).sceneManagerSetupRestored
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
This can be useful to get notified when the SceneManager's scenes are replaced with a set of new scenes from calls to [RestoreSceneManagerSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.RestoreSceneManagerSetup.html).  
  
Use the `scenes` argument to check what scenes has just been opened.  
  
Additional resources: [SceneManagerSetupRestoredCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SceneManagerSetupRestoredCallback.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor.SceneManagement;  
  
[InitializeOnLoad]
class CheckRestoredScenes
{
    static CheckRestoredScenes()
    {
        EditorSceneManager.sceneManagerSetupRestored[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager-sceneManagerSetupRestored.html) += OnSceneManagerSetupRestored;
    }  
  
    static void OnSceneManagerSetupRestored(Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)[] scenes)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnSceneManagerSetupRestored: restored " + scenes.Length);
    }
}
```

* * *
