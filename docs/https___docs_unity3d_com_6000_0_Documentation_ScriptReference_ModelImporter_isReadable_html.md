* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-isReadable.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).isReadable
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
isReadable; 
### Description
Are mesh vertices and indices accessible from script?
Making a mesh readable will keep two copies of it in memory, one for rendering and one in system memory for script access. Setting isReadable to false therefore saves memory. Scaling a mesh with different amounts along the three axes (i.e. non-uniform scaling) requires the mesh to be readable for correct lighting.  
  
In the Unity editor access is always permitted when not in play mode.
* * *
