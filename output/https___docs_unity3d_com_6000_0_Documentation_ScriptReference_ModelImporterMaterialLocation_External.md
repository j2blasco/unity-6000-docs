* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialLocation.External.html

#  [ModelImporterMaterialLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialLocation.html).External
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
Extract the materials and textures from the model.
Unity extracts the materials to the Materials folder, at the same level as the model file. Unity also extracts the embedded textures to the folder named <modelName>.fbm.  
  
For example, if the model is Assets/Model/MyModel.fbx, then its materials are extracted to Assets/Model/Materials, and the embedded textures are extracted to Assets/Model/MyModel.fbm.  
  
Note: if the Materials folder already contains a material with the same name as a material being extracted, Unity does not replace the existing material.
* * *
