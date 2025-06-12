* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-avatarSetup.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).avatarSetup
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
[ModelImporterAvatarSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAvatarSetup.html) avatarSetup; 
### Description
The Avatar generation of the imported model.
This property depends on the value of [ModelImporter.animationType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-animationType.html):  
  
- [ModelImporterAnimationType.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAnimationType.None.html) or [ModelImporterAnimationType.Legacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAnimationType.Legacy.html) sets this property to [ModelImporterAvatarSetup.NoAvatar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAvatarSetup.NoAvatar.html) because Avatar generation does not support the None or Legacy animation types.  
  
- [ModelImporterAnimationType.Generic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAnimationType.Generic.html) supports any value.  
  
- [ModelImporterAnimationType.Human](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAnimationType.Human.html) requires an avatar to import its animation. You must use either [ModelImporterAvatarSetup.CreateFromThisModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAvatarSetup.CreateFromThisModel.html), [ModelImporterAvatarSetup.CopyFromOther](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAvatarSetup.CopyFromOther.html) or set ModelImporterAvatarSetup.autoGenerateAvatarMappingIfUnspecified to true .
* * *
