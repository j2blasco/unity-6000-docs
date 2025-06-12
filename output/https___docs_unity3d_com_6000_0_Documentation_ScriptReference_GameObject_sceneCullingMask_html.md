* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-sceneCullingMask.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).sceneCullingMask
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
sceneCullingMask; 
### Description
The Scene culling mask defined for the GameObject. (Read Only)
Unity uses [SceneCullingMasks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.html) to determine which scene to render the GameObject in. The `sceneCullingMask` is a bitfield stored as an unsigned 64-bit integer [ulong](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types). Cameras only render an object in a scene if the bits set on the Scene's mask (retrievable with[EditorSceneManager.GetSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.GetSceneCullingMask.html)) match those in the object's `sceneCullingMask`. 
```
using UnityEngine;
using UnityEditor.SceneManagement;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    
    void Start()
    {
        //Check if gameObject is visible in scene
        if(gameObject.sceneCullingMask == EditorSceneManager.GetSceneCullingMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.GetSceneCullingMask.html)(gameObject.scene))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Object is visible");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Object is not visible");
        }
    }
}

```

Additional resources: [SceneCullingMasks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.html), [Camera.overrideSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-overrideSceneCullingMask.html), [EditorSceneManager.SetSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SetSceneCullingMask.html)
* * *
