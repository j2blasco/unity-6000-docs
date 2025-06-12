* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.html

# ModelImporterNormalCalculationMode
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
Normal generation options for [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).
Normals can be calculated by Unity using several methods. They can be either unweighted or weighted by area, angle or both.  
  
Additional resources: ModelImporter.normalImportMode.
### Properties
Property | Description  
---|---  
[Unweighted_Legacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.Unweighted_Legacy.html) | The normals are unweighted. This option uses the legacy algorithm for handling hard edges.  
[Unweighted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.Unweighted.html) | The normals are not weighted.  
[AreaWeighted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.AreaWeighted.html) | The normals are weighted by the face area.  
[AngleWeighted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.AngleWeighted.html) | The normals are weighted by the vertex angle on each face.  
[AreaAndAngleWeighted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.AreaAndAngleWeighted.html) | The normals are weighted by both the face area and the vertex angle on each face.  
* * *
