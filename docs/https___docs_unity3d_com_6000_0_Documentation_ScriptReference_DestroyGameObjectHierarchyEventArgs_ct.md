* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs-ctor.html

# DestroyGameObjectHierarchyEventArgs Constructor
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
public DestroyGameObjectHierarchyEventArgs(int instanceId, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
## Declaration
public DestroyGameObjectHierarchyEventArgs(int instanceId, int parentInstanceId, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
instanceId | The instance ID of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has been destroyed.  
parentInstanceId | The instance ID for the parent [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has been destroyed.  
scene | The [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) containing the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has been destroyed.  
### Description
Constructs a new instance.
* * *
