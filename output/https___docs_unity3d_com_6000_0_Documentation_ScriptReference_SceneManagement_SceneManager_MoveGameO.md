* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.MoveGameObjectsToScene.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).MoveGameObjectsToScene
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
public static void MoveGameObjectsToScene(NativeArray<int> instanceIDs, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
instanceIDs | GameObjects by instance ID to move.  
scene | Scene to move into.  
### Description
Move multiple GameObjects, represented by a NativeArray of instance IDs, from their current Scene to a new Scene.
You can only move root GameObjects from one Scene to another. This means the GameObject to move must not be a child of any other GameObject in its Scene. This only works on GameObjects being moved to a Scene that is already loaded (additive). If you want to load single Scenes, make sure to use DontDestroyOnLoad on the GameObject you would like to move to a new Scene, otherwise Unity deletes it when it loads a new Scene.
* * *
