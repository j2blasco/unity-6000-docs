* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneUtility.GetBuildIndexByScenePath.html

#  [SceneUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneUtility.html).GetBuildIndexByScenePath
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
public static int GetBuildIndexByScenePath(string scenePath); 
### Parameters
Parameter | Description  
---|---  
scenePath | Scene path (e.g: "Assets/Scenes/Scene1.unity").  
### Returns
**int** Build index. 
### Description
Get the build index from a Scene path.
The build index refers to the index into the list of Scenes as specified in the Build Settings window.  
  
If the scene isn't found it returns -1.
* * *
