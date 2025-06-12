* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html

# Asset
class in UnityEditor.VersionControl
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
This class containes information about the version control state of an asset.
### Properties
Property | Description  
---|---  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-assetPath.html) | Gets the path of the Asset relative to the project root. If the Asset is a meta file, the path to the meta file is returned.  
[fullName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-fullName.html) | Gets the full name of the asset including extension.  
[isFolder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-isFolder.html) | Returns true if the asset is a folder.  
[isInCurrentProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-isInCurrentProject.html) | Returns true if the asset file exists and is in the current project.  
[isMeta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-isMeta.html) | Returns true if the instance of the Asset class actually refers to a .meta file.  
[locked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-locked.html) | Returns true if the asset is locked by the version control system.  
[metaPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-metaPath.html) | Gets the path of the meta file for this Asset relative to the project root. If the Asset is a meta file, the path to the meta file is returned.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-name.html) | Get the name of the asset.  
[path](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-path.html) | Gets the path of the asset.  
[readOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-readOnly.html) | Returns true is the asset is read only.  
[state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset-state.html) | Gets the version control state of the asset.  
### Public Methods
Method | Description  
---|---  
[Edit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.Edit.html) | Opens the assets in an associated editor.  
[IsOneOfStates](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.IsOneOfStates.html) | Returns true if the version control state of the assets is one of the input states.  
[IsState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.IsState.html) | Returns true if the version control state of the asset exactly matches the input state.  
[Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.Load.html) | Loads the asset to memory.  
* * *
