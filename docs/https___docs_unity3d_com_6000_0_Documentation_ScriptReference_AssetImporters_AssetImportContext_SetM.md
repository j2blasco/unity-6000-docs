* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.SetMainObject.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).SetMainObject
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
public void SetMainObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
### Parameters
Parameter | Description  
---|---  
obj | The object to be set as the main object. This object must already be added with the AddObjectToAsset method.  
### Description
Sets the main object for import.
Use this method to specify the main object in the asset file.  
  
Note: Before invoking this method, the object that is passed as the argument must first be added with AddObjectToAsset. If this method is not called, then one of the objects added through AddObjectToAsset is arbitrarily promoted as the main object. If objects of type [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) are added through AddObjectToAsset, then SetMainObject must refer to one of these objects. Passing a different type of object results in the selection being ignored and an arbitrary GameObjects is promoted as the main object.  
  
Note: This method returns an error when used in an AssetPostprocessor because the Importer sets the main object later in the import process.
* * *
