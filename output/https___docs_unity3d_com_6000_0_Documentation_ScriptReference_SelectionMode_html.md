* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.html

# SelectionMode
enumeration
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
SelectionMode can be used to tweak the selection returned by Selection.GetTransforms.
The default transform selection mode is: [SelectionMode.TopLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.TopLevel.html) | [SelectionMode.ExcludePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.ExcludePrefab.html) | [SelectionMode.Editable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Editable.html).
### Properties
Property | Description  
---|---  
[Unfiltered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Unfiltered.html) | Return the whole selection.  
[TopLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.TopLevel.html) | Only return the topmost selected transform. A selected child of another selected transform will be filtered out.  
[Deep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Deep.html) | Return the selection and all child transforms of the selection.  
[ExcludePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.ExcludePrefab.html) | Excludes any Prefabs from the selection.  
[Editable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Editable.html) | Excludes any objects which shall not be modified.  
[Assets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Assets.html) | Only return objects that are assets in the Asset directory.  
[DeepAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.DeepAssets.html) | If the selection contains folders, also include all assets and subfolders within that folder in the file hierarchy.  
* * *
