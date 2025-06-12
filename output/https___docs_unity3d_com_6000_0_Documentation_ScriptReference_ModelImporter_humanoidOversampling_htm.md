* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-humanoidOversampling.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).humanoidOversampling
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
[ModelImporterHumanoidOversampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterHumanoidOversampling.html) humanoidOversampling; 
### Description
Controls how much oversampling is used when importing humanoid animations for retargeting.
Humanoid retargeting implies resampling animations at import. By default, the sampling rate of the imported file is used. There are exceptional cases where a higher sampling rate is needed to ensure valid interpolation between original frames. Key reducing can be used on top of oversampling to reduce the size of the final produced clip. Key reducing will not remove keys where tighter interpolation is needed.
* * *
