* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-importMaterials.html

**Removed**   

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).importMaterials
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
**Obsolete** importMaterials has been removed. Use materialImportMode instead. public bool importMaterials; 
### Description
Import materials from file.
When set to false ModelImporter will use default material (Default-Diffuse.mat) instead of imported materials, otherwise it will find existing or create new materials based on [materialName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialName.html) and [materialSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialSearch.html) options.  
  
Additional resources: [materialName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialName.html), [materialSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-materialSearch.html) options.
* * *
