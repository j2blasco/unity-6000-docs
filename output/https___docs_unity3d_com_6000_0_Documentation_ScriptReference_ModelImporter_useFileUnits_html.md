* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-useFileUnits.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).useFileUnits
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
useFileUnits; 
### Description
Detect file units and import as 1FileUnit=1UnityUnit, otherwise it will import as 1cm=1UnityUnit.
This setting is used only for .max files. It was introduced for backwards compatibility: there is a bug in some FBX 2011 plugins - they fail to pick up file units and export everything as 1unit=1cm. We fixed that problem by setting the units manually, but that breaks projects which were built with FBX 2011 plugins already, so useFileUnits was introduced as a solution. Set it to false if you want to default to centimeters in FBX exporter.  
  
Additional resources: [isUseFileUnitsSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-isUseFileUnitsSupported.html).
* * *
