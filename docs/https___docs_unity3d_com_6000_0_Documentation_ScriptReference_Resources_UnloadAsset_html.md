* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadAsset.html

#  [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html).UnloadAsset
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
public static void UnloadAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetToUnload); 
### Description
Unloads `assetToUnload` from memory.
This function can only be called on Assets that are stored on disk.  
  
The referenced asset (assetToUnload) will be unloaded from memory. The object will become invalid and can't be loaded back from disk. Any subsequently loaded Scenes or assets that reference the asset on disk will cause a new instance of the object to be loaded from disk. This new instance will not be connected to the previously unloaded object.
* * *
