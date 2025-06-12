* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ExecuteMenuItem.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).ExecuteMenuItem
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
public static bool ExecuteMenuItem(string menuItemPath); 
### Description
Invokes the menu item in the specified path.
This function also works with Editor Scripts.
```
// Simple script that lets you create a new
// Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), create a cube and an empty game object in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
// Save the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and close the editor  
  
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SceneManagement;  
  
public class ExampleClass
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Execute menu items")]
    static void EditorPlaying()
    {
        var newScene = EditorSceneManager.NewScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewScene.html)(NewSceneSetup.EmptyScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneSetup.EmptyScene.html), NewSceneMode.Single[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneMode.Single.html));  
  
        EditorApplication.ExecuteMenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ExecuteMenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/3D Object/Cube");
        EditorApplication.ExecuteMenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ExecuteMenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Create Empty");  
  
        EditorSceneManager.SaveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveScene.html)(newScene, "Assets/MyNewScene.unity");
        EditorApplication.Exit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Exit.html)(0);
    }
}

```

* * *
