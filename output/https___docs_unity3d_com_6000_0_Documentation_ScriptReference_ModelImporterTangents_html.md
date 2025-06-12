* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.html

# ModelImporterTangents
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
Vertex tangent generation options for [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).
Tangentss can either be imported from model file, calculated by Unity using several methods (default is MikkTSpace), or not included into imported mesh at all. Vertex tangents are most often used for normal/bump mapping.  
  
Additional resources: [ModelImporter.importTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importTangents.html), [ModelImporterNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormals.html), [Mesh.tangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-tangents.html).
### Properties
Property | Description  
---|---  
[Import](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.Import.html) | Import vertex tangents from model file.  
[CalculateLegacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.CalculateLegacy.html) | Calculate tangents with legacy algorithm.  
[CalculateLegacyWithSplitTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.CalculateLegacyWithSplitTangents.html) | Calculate tangents with legacy algorithm, with splits across UV charts.  
[CalculateMikk](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.CalculateMikk.html) | Calculate tangents using MikkTSpace (default).  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.None.html) | Do not import vertex tangents.  
* * *
