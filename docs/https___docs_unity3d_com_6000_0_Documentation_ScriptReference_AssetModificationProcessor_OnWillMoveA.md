* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillMoveAsset.html

#  [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html).OnWillMoveAsset(string,string)
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
### Description
Unity calls this method when it is about to move an Asset on disk.
Implement this method to customize the actions Unity performs when moving an Asset inside the Editor. This method allows you to move the Asset yourself but, if you do, please remember to return the correct enum. Alternatively, you can perform some processing and let Unity move the file. The moving of the asset can be prevented by returning [AssetMoveResult.FailedMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetMoveResult.FailedMove.html) You should not call any Unity AssetDatabase API from within this callback, preferably restrict yourself to the usage of file operations or VCS APIs.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class CustomAssetModificationProcessor : UnityEditor.AssetModificationProcessor
{
    private static AssetMoveResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetMoveResult.html) OnWillMoveAsset(string sourcePath, string destinationPath)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Source path: " + sourcePath + ". Destination path: " + destinationPath + ".");
        AssetMoveResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetMoveResult.html) assetMoveResult = AssetMoveResult.DidMove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetMoveResult.DidMove.html);  
  
        // Perform operations on the asset and set the value of 'assetMoveResult' accordingly.  
  
        return assetMoveResult;
    }
}

```

* * *
