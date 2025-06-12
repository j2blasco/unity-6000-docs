* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-loadedSceneCount.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).loadedSceneCount
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
loadedSceneCount; 
### Description
The number of loaded Scenes.
Returns the current number of loaded Scenes. This doesn't include the Scenes that are currently loading or unloading. For the total number of Scenes see [SceneManager.sceneCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneCount.html).
```
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    // adds a custom menu item which displays the number of open Scenes in a Dialogue Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("SceneExample/Number Of Scenes")]
    public static void NumberOfScenes()
    {
        EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Number of loaded Scenes:", SceneManager.loadedSceneCount.ToString(), "OK");
    }
}

```

* * *
