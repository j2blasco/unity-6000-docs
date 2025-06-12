* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalSmoothingSource.html

# ModelImporterNormalSmoothingSource
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
Source of smoothing information for calculation of normals in [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).
Describes how Unity calculates whether edges have hard or smooth normals (from smoothing groups or the angle between faces). By default, Unity uses smoothing groups if they are present. If not, it uses angles.  
  
Additional resources: [ModelImporter.normalSmoothingSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-normalSmoothingSource.html), [Mesh.normals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-normals.html).
### Properties
Property | Description  
---|---  
[PreferSmoothingGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalSmoothingSource.PreferSmoothingGroups.html) | Use smoothing groups if they are present in the Model file, otherwise use angle (default).  
[FromSmoothingGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalSmoothingSource.FromSmoothingGroups.html) | Use smoothing groups to determine which edges are smooth and which are hard.  
[FromAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalSmoothingSource.FromAngle.html) | Use the angle between adjacent faces to determine if an edge is smooth or hard.  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalSmoothingSource.None.html) | Do not create hard edges.  
* * *
