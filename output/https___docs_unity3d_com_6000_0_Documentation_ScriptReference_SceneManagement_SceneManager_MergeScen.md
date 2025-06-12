* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.MergeScenes.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).MergeScenes
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
public static void MergeScenes([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) sourceScene, [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) destinationScene); 
### Parameters
Parameter | Description  
---|---  
sourceScene | The Scene that will be merged into the destination Scene.  
destinationScene | Existing Scene to merge the source Scene into.  
### Description
This will merge the source Scene into the destinationScene.
This function merges the contents of the source Scene into the destination Scene, and deletes the source Scene. All GameObjects at the root of the source Scene are moved to the root of the destination Scene.  
**Note:** This function is destructive: The source Scene will be destroyed once the merge has been completed. 
* * *
