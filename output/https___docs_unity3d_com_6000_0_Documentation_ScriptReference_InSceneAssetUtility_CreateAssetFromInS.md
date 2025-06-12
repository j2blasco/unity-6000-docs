* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CreateAssetFromInSceneAsset.html

#  [InSceneAssetUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.html).CreateAssetFromInSceneAsset
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
public static bool CreateAssetFromInSceneAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) inSceneAsset, string filePath); 
### Parameters
Parameter | Description  
---|---  
inSceneAsset | The in-scene asset object to convert to a project asset.  
filePath | The file path for the new asset. The path is relative to the project folder.  
### Returns
**bool** True if the project asset was created successfully. 
### Description
Creates a project asset from the given in-scene asset and saves it at the provided file path.
Any in-scene assets referenced by the provided `inSceneAsset` are saved as sub-objects of the new asset.   
  
Note that `filePath` is relative to the project folder, for example: "Assets/MyStuff/hello.mat". For more details on `filePath` requirements see [AssetDatabase.CreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html).  
  
Additional resources: [InSceneAssetUtility.CreateInSceneAssetFromAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.CreateInSceneAssetFromAsset.html).
* * *
