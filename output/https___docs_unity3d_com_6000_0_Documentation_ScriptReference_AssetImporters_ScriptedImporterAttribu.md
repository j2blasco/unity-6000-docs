* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterAttribute-importQueuePriority.html

#  [ScriptedImporterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterAttribute.html).importQueuePriority
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
importQueuePriority; 
### Description
Enables controlling the ordering of asset import based on type. Positive values delay the processing of source asset files while negative values place them earlier in the import process.
This allows for basic dependency of asset imports. For example, having a custom asset type that must be run after all image files have been imported or after another type of custom importer has executed.   
Useful values range between -3000 and greater than zero. Negative values allow the execution to occur before native importers are run (each native type has its own queue order).
* * *
