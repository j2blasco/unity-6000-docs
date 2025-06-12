* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.InitializeExtraDataInstance.html

#  [AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html).InitializeExtraDataInstance
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
protected void InitializeExtraDataInstance([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) extraData, int targetIndex); 
### Parameters
Parameter | Description  
---|---  
extraData | A ScriptableObject instance of the type provided by [AssetImporterEditor.extraDataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataType.html).  
targetIndex | The corresponding [Editor.targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-targets.html) index of the provided extraData.  
### Description
This method is called during the initialization process of the Editor, after Awake and before OnEnable.
If the AssetImporterEditor have the [CanEditMultipleObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html) attribute and more than one Importer is selected, this method will be called once for each [extraDataTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataTargets.html) using targetIndex to find the corresponding [Editor.targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-targets.html) Importer.  
  
Note: Assembly reloading or external changes made to the inspected file in the Editor may trigger this method outside of the initialization loop. However, you should always reset your data in the given object when it gets called to make sure you stay up to date with the asset file.  
  
See a usage example at [AssetImporterEditor.extraDataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataType.html).
* * *
