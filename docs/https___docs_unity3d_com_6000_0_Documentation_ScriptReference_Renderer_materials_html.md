* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-materials.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).materials
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
materials; 
### Description
Returns all the instantiated materials of this object.
This is an array of all materials used by the renderer. Unity supports a single object using multiple materials; in this case `materials` contains all the materials. [sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterial.html) and [material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html) properties return the first used material if there is more than one.  
  
Modifying any material in `materials` will change the appearance of only that object.  
  
Note that like all arrays returned by Unity, this returns a copy of materials array. If you want to change some materials in it, get the value, change an entry and set materials back.  
  
**Note:**  
This function automatically instantiates the materials and makes them unique to this renderer. It is your responsibility to destroy the materials when the game object is being destroyed. [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) also destroys the materials but it is usually only called when loading a new level.
* * *
