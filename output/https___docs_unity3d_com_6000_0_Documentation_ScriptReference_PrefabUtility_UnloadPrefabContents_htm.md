* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnloadPrefabContents.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).UnloadPrefabContents
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
public static void UnloadPrefabContents([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) contentsRoot); 
### Parameters
Parameter | Description  
---|---  
contentsRoot | The root of the loaded Prefab contents.  
### Description
Releases the content from a Prefab previously loaded with LoadPrefabContents from memory.
This will destroy the GameObject in memory and release the isolated Scene used to contain the Prefab content.  
  
The root GameObject will not be available after this call. The Prefab Asset itself is not affected by this call.  
  
Additional resources: [PrefabUtility.LoadPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.LoadPrefabContents.html), [PrefabUtility.SaveAsPrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html), [EditPrefabContentsScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.EditPrefabContentsScope.html).
* * *
