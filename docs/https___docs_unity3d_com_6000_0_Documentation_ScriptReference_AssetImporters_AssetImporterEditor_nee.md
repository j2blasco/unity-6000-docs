* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-needsApplyRevert.html

#  [AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html).needsApplyRevert
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
needsApplyRevert; 
### Description
Whether the ApplyRevertGUI method is required to draw in the Inspector.
Most Importers expose settings that are changed by users and require the Apply/Revert button to be pressed to update settings changes. Some Importers, such as MonoScriptImporter, do not expose settings and do not require the use of the ApplyRevertGUI method to update changes. In the cases where ApplyRevertGUI is not required, you can override needApplyRevert to return false. This avoids unnecessary checks on assets that the Importer Inspector performs when it is closed.
* * *
