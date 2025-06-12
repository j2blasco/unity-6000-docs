* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetsToTrash.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).MoveAssetsToTrash
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
public static bool MoveAssetsToTrash(string[] paths, List<string> outFailedPaths); 
### Parameters
Parameter | Description  
---|---  
paths | Project relative paths of the assets or folders to be deleted.  
outFailedPaths | Project relative paths which could not be deleted.  
### Returns
**bool** Returns true if all assets in paths have successfully been deleted, false if any of the specified paths don't exist or couldn't be removed. 
### Description
Lets you move multiple assets or folders to trash at once with performance benefits under version control.
Paths should be relative to the project folder, for example: "Assets/MyTextures/hello.png"  
  
This should be used instead of [AssetDatabase.MoveAssetToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetToTrash.html) for performance reasons when opearating on many assets at once with active version control integration.  
  
Note that the speedup will only be present when using Asset Database v2. Also note that files which are under version control are not guaranteed to end up in the OS trash bin as they are removed by the versin control system itself.  
  
Additional resources: [AssetDatabase.DeleteAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAsset.html), [AssetDatabase.MoveAssetToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetToTrash.html), [AssetDatabase.MoveAssetsToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetsToTrash.html).
* * *
