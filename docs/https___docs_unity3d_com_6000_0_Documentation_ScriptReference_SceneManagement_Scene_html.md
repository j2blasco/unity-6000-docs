* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html

# Scene
struct in UnityEngine.SceneManagement
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Run-time data structure for *.unity file.
### Properties
Property | Description  
---|---  
[buildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-buildIndex.html) | Return the index of the Scene in the Build Settings.  
[isDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-isDirty.html) | Returns true if the Scene is modified.  
[isLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-isLoaded.html) | IsLoaded is set to true after loading has completed and objects have been enabled.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-name.html) | Returns the name of the Scene that is currently active in the game or app.  
[path](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-path.html) | Returns the relative path of the Scene. For example: "Assets/MyScenes/MyScene.unity".  
[rootCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-rootCount.html) | The number of root transforms of this Scene.  
### Public Methods
Method | Description  
---|---  
[GetRootGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.GetRootGameObjects.html) | Returns all the root game objects in the Scene.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.IsValid.html) | Whether this is a valid Scene. A Scene may be invalid if, for example, you tried to open a Scene that does not exist. In this case, the Scene returned from EditorSceneManager.OpenScene would return False for IsValid.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-operator_ne.html) | Returns true if the Scenes are different.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene-operator_eq.html) | Returns true if the Scenes are equal.  
* * *
