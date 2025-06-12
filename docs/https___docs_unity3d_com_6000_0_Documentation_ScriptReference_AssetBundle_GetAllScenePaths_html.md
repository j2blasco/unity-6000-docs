* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.GetAllScenePaths.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).GetAllScenePaths
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
public string[] GetAllScenePaths(); 
### Description
Return all the names of Scenes in the AssetBundle.
Only works for streamed Scene AssetBundles, otherwise an empty string array is returned. The names are the project-relative path of each .unity file, unless a different name was specified at build time.  
  
Additional resources: [AssetBundle.isStreamedSceneAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle-isStreamedSceneAssetBundle.html), [SceneManager.LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html), [AssetBundleBuild.addressableNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-addressableNames.html)
* * *
