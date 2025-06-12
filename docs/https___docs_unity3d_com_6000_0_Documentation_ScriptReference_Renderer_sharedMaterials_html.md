* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterials.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).sharedMaterials
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
sharedMaterials; 
### Description
All the shared materials of this object.
This is an array of all materials used by the renderer. Unity supports multiple objects using a single material; in this case `sharedMaterials` contains all the materials used for this. [sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterial.html) and [material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html) properties return the first used material if there is more than one.  
  
Modifying any material in `sharedMaterials` will change the appearance of all objects using this material, and change material settings that are stored in the project too.  
  
It is not recommended to modify materials returned by sharedMaterials. If you want to modify the material of a renderer use [material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html) instead.  
  
Note that like all arrays returned by Unity, this returns a copy of materials array. If you want to change some materials in it, get the value, change an entry and set materials back.  
  
Additional resources: [material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html), [sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterial.html) properties.
* * *
