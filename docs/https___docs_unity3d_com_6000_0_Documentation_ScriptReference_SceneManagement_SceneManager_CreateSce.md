* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.CreateScene.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).CreateScene
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
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) CreateScene(string sceneName); 
## Declaration
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) CreateScene(string sceneName, [SceneManagement.CreateSceneParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.CreateSceneParameters.html) parameters); 
### Parameters
Parameter | Description  
---|---  
sceneName | The name of the new Scene. It cannot be empty or null, or same as the name of the existing Scenes.  
parameters | Various parameters used to create the Scene.  
### Returns
**Scene** A reference to the new Scene that was created, or an invalid Scene if creation failed. 
### Description
Create an empty new Scene at runtime with the given name.
The new Scene will be opened additively into the hierarchy alongside any existing Scenes that are currently open. The path of the new Scene will be empty. This function is for creating Scenes at runtime. To create a Scene at edit-time (for example, when making an editor script or tool which needs to create Scenes), use [EditorSceneManager.NewScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewScene.html).
```
using UnityEngine.SceneManagement;
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Awake()
    {
        Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) newScene = SceneManager.CreateScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.CreateScene.html)("My New Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)");
    }
}

```

* * *
