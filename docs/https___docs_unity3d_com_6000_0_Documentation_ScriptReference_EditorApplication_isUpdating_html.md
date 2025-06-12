* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isUpdating.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).isUpdating
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
isUpdating; 
### Description
True if the Editor is currently refreshing the AssetDatabase.
During AssetDatabase refreshing time, the editor checks to see if any files have changed, whether they need to be reimported, and reimports them. The isUpdating property will return true or false depending on whether the AssetDatabase is being loaded or not. (Read Only)
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class NewSceneWhileNotUpdating
{
    // Simple editor Script that lets you create a new
    // Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) if editor is not updating.  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/New Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) while not updating")]
    static void EditorPlaying()
    {
        if (!EditorApplication.isUpdating[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isUpdating.html))
        {
            EditorApplication.NewScene();
        }
    }
}

```

* * *
