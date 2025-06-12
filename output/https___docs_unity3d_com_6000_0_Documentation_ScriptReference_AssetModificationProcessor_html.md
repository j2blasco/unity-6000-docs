* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html

# AssetModificationProcessor
class in UnityEditor
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
AssetModificationProcessor lets you hook into saving of serialized assets and scenes which are edited inside Unity.
This lets you prevent writing of assets by Unity for integration with VCS solutions like Perforce which require locking of files.  
  
This can be used as a callback to know when Assets are saved. You can then make actions such as run code generator. 
### Messages
Message | Description  
---|---  
[CanOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.CanOpenForEdit.html) | This is called by Unity when inspecting assets to determine if they can potentially be opened for editing.  
[FileModeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.FileModeChanged.html) | Unity calls this method when file mode has been changed for one or more files.  
[IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.IsOpenForEdit.html) | This is called by Unity when inspecting assets to determine if an editor should be disabled.  
[MakeEditable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.MakeEditable.html) | Unity calls this method when one or more files need to be opened for editing.  
[OnWillCreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillCreateAsset.html) | Unity calls this method when it is about to create an Asset you haven't imported (for example, .meta files).  
[OnWillDeleteAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillDeleteAsset.html) | This is called by Unity when it is about to delete an asset from disk.  
[OnWillMoveAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillMoveAsset.html) | Unity calls this method when it is about to move an Asset on disk.  
[OnWillSaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillSaveAssets.html) | This is called by Unity when it is about to write serialized assets or Scene files to disk.  
* * *
