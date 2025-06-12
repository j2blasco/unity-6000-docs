* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneAt.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).GetSceneAt
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
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) GetSceneAt(int index); 
### Parameters
Parameter | Description  
---|---  
index | Index of the Scene to get. Index must be greater than or equal to 0 and less than SceneManager.sceneCount.  
### Returns
**Scene** A reference to the Scene at the index specified. 
### Description
Get the Scene at index in the SceneManager's list of loaded Scenes.
```
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.SceneManagement;  
  
public class Example
{
    // adds a menu item which gives a brief summary of currently open Scenes
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("SceneExample/Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Summary")]
    public static void ListSceneNames()
    {
        StringBuilder sb;  
  
        if (SceneManager.sceneCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneCount.html) > 0)
        {
            sb = new StringBuilder();
            for (int n = 0; n < SceneManager.sceneCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneCount.html); ++n)
            {
                Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene = SceneManager.GetSceneAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneAt.html)(n);
                sb.Append(scene.name);
                sb.Append(scene.isLoaded ? " (Loaded, " : " (Not Loaded, ");
                sb.Append(scene.isDirty ? "Dirty, " : "Clean, ");
                sb.Append(scene.buildIndex >= 0 ? " in build)\n" : " NOT in build)\n");
            }
        }
        else
        {
            sb = new StringBuilder("No open Scenes.");
        }
        EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Summary", sb.ToString(), "OK");
    }
}

```

* * *
