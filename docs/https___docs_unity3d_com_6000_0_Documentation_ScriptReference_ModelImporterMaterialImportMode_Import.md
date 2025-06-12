* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialImportMode.ImportViaMaterialDescription.html

#  [ModelImporterMaterialImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialImportMode.html).ImportViaMaterialDescription
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
The model importer creates materials using the PreprocessMaterialDescription AssetPostprocessor.
When selected, the model importer delegates the process of populating new material properties to OnPreprocessMaterialDescription AssetPostprocessor In this mode, the model importer collects all available properties and animation data read from imported materials into a MaterialDescription struct. An internal implementation read most of the values and animation data from these properties and automatically re-map them to the Standard Unity Shader. HDRP and UniversalRP packages also provide their own implementations that remap the fbx material properties and animations to the Standard shader of the currently active rendering pipeline. When selected, OnPostprocessMaterial AssetPostprocessor is not called by the Model Importer. Additional resources: [AssetPostprocessor.OnPreprocessMaterialDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessMaterialDescription.html).
* * *
