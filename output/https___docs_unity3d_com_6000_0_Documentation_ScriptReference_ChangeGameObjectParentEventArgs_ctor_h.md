* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectParentEventArgs-ctor.html

# ChangeGameObjectParentEventArgs Constructor
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
public ChangeGameObjectParentEventArgs(int instanceId, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) previousScene, int previousParentInstanceId, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) newScene, int newParentInstanceId); 
### Parameters
Parameter | Description  
---|---  
instanceId | The instance ID of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) whose parent changed. Note that this is not the instance ID of the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component.  
previousScene | The scene containing the previous parent. This is useful to detect whether a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) was moved to another scene.  
previousParentInstanceId | The instance ID of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that was the previous parent of the target. Note that this is not the instance ID of its [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).  
newScene | The [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) containing the new parent. This is useful to detect whether a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) was moved to another scene or moved to the root of a scene.  
newParentInstanceId | The instance ID of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that is the new parent of the target. Note that this is not the instance ID of its [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).  
### Description
Constructs a new instance.
* * *
