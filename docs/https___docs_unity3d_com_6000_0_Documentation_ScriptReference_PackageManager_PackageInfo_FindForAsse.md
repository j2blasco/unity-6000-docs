* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.FindForAssetPath.html

#  [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html).FindForAssetPath
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html "Go to PackageManager Component in the Manual")
## Declaration
public static PackageInfo FindForAssetPath(string assetPath); 
### Parameters
Parameter | Description  
---|---  
assetPath | The file path of the asset.  
### Returns
**PackageInfo** The [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) instance describing the package, or null if the asset is not in a package. 
### Description
Retrieves information about the package containing an asset based on the path of that asset.
* * *
