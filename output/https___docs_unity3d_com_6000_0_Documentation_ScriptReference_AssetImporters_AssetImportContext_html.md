* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html

# AssetImportContext
class in UnityEditor.AssetImporters
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
Defines the import context for scripted importers during an import event.
This class carries both input and output information for the OnImportAsset() task.
### Properties
Property | Description  
---|---  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext-assetPath.html) | The path of the source asset file to be imported.  
[mainObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext-mainObject.html) | The main object set on the AssetImportContext.  
[selectedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext-selectedBuildTarget.html) | Returns the current build target and creates a dependency on the target platform within a scripted importer.  
### Public Methods
Method | Description  
---|---  
[AddObjectToAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.AddObjectToAsset.html) | Adds an object to the result of the import operation.  
[DependsOnArtifact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnArtifact.html) | Setup artifact dependency to an asset.  
[DependsOnCustomDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnCustomDependency.html) | Allows you to specify that an Asset has a custom dependency.  
[DependsOnSourceAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnSourceAsset.html) | Allows you to specify that an Asset depends directly on the source file of another Asset (as opposed to the import result of another asset).  
[GetArtifactFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetArtifactFilePath.html) | Returns the path of the Artifact file that was created by another importer, and adds a dependency to that file.  
[GetObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetObjects.html) | Gets the list of objects set on the AssetImportContext.  
[GetOutputArtifactFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html) | Returns the path where to write a new Artifact File with the given fileName.  
[GetReferenceToAssetMainObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetReferenceToAssetMainObject.html) | Returns the main asset from the given path (if it exists) and automatically adds a dependency on its path if it is the main asset type.  
[LogImportError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.LogImportError.html) | Logs an error message encountered during import.  
[LogImportWarning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.LogImportWarning.html) | Logs a warning message encountered during import.  
[SetMainObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.SetMainObject.html) | Sets the main object for import.  
* * *
