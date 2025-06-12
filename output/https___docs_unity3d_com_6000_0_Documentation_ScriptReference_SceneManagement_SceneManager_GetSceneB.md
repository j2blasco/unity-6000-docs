* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetSceneByName.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).GetSceneByName
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
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) GetSceneByName(string name); 
### Parameters
Parameter | Description  
---|---  
name | Name of Scene to find.  
### Returns
**Scene** A reference to the Scene, if valid. If not, an invalid Scene is returned. 
### Description
Searches through the Scenes loaded for a Scene with the given name.
The name has to be without the .unity extension. The name can be the last part of the name as displayed in the BuildSettings window in which case the first Scene that matches will be returned. The name can also be the path as displayed in the Build Settings (still without the .unity extension), in which case only the exact match will be returned. This is case insensitive.
* * *
