* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetMaterialProperties.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).GetMaterialProperties
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
public static MaterialProperty[] GetMaterialProperties(Object[] mats); 
### Parameters
Parameter | Description  
---|---  
mats | The selected materials.  
### Returns
**MaterialProperty[]** Returns the material properties. 
### Description
Get shader property information of the materials you pass in.
When implementing custom MaterialEditors, you'd usually pass the `this.targets` array to this function, where `this.targets` is all the selected materials.  
  
Additional resources: [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html).
* * *
