* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.GetMaterials.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).GetMaterials
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
## Declaration
public void GetMaterials(List<Material> m); 
### Parameters
Parameter | Description  
---|---  
m | A list of materials to populate.  
### Description
Returns all the instantiated materials of this object.
Use this method instead of [materials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-materials.html) if you control the life cycle of the list passed in and you want to avoid allocating a new array with every access.
* * *
