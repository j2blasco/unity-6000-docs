* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SavePrefabAsset.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).SavePrefabAsset
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) SavePrefabAsset([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) asset); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) SavePrefabAsset([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) asset, out bool savedSuccessfully); 
### Parameters
Parameter | Description  
---|---  
asset | Any GameObject that is part of the Prefab Asset to save.  
savedSuccessfully | The result of the save action, either successful or unsuccessful. Use this together with the console log to get more insight into the save process.  
### Returns
**GameObject** The root GameObject of the saved Prefab Asset. 
### Description
Saves the version of an existing Prefab Asset that exists in memory back to disk.
The given object has to be a GameObject from an existing Prefab Asset. If you have a GameObject from a Prefab instance and get the corresponding object, you will have the corresponding GameObject from the Prefab Asset.  
  
Additional resources: [PrefabUtility.SaveAsPrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html), [PrefabUtility.GetCorrespondingObjectFromSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetCorrespondingObjectFromSource.html).
* * *
