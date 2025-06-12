* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.AddObjectToAsset.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).AddObjectToAsset
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
public void AddObjectToAsset(string identifier, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public void AddObjectToAsset(string identifier, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) thumbnail); 
### Parameters
Parameter | Description  
---|---  
identifier | A unique identifier associated to this object.  
obj | The Unity Object to add to the asset.  
thumbnail | An optional 2D texture to use as the thumbnail for this object.  
### Description
Adds an object to the result of the import operation.
Use this method to add objects to the resulting asset. AddObjectToAsset can be called multiple times if more than one unity object is the result of the import process. Note: You must make sure that your importer provides a unique identifier for each added object. You must also make sure that your code regenerates the same identifier each time the file is re-imported: identifiers should be deterministic. This allows Unity to keep match previously imported objects with the newly created objects. The identifier only needs to be unique within the context of the Asset file and not globally unique across your whole project.
* * *
