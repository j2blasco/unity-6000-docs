* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.PostProcessSceneAttribute.html

# PostProcessSceneAttribute
class in UnityEditor.Callbacks
/
Inherits from:[CallbackOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CallbackOrderAttribute.html)
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
Add this attribute to a method to get a notification just after building the Scene.
A method with this attribute will also get called when entering Playmode, when [SceneManager.LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html) is called.  
  
`PostProcessSceneAttribute` has an option to provide an order index in the callback, starting at 0. This is useful if you have more than one OnPostprocessScene callback, and you would like them to be called in a certain order. Callbacks are called in order, starting at zero.  
  
**Note:** If there are no new changes to the scene since the previous Player build, Unity doesn't rebuild the scene but uses cached Player data instead. In this case the `PostProcessSceneAttribute` callback is not called. To ensure an unchanged scene rebuilds, you can either mark the scene dirty with [EditorSceneManager.MarkSceneDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.MarkSceneDirty.html) or clear the build cache with [BuildOptions.CleanBuildCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CleanBuildCache.html).  
  
Additional resources: [IProcessSceneWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.html)
```
// C# example:
// Automatically creates a game object with a primitive mesh renderer and appropriate collider.
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Callbacks;  
  
public class MyScenePostprocessor {
    [PostProcessSceneAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.PostProcessSceneAttribute.html) (2)]
    public static void OnPostprocessScene() {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        cube.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.5f, 0.0f);
    }
}

```

### Inherited Members
* * *
