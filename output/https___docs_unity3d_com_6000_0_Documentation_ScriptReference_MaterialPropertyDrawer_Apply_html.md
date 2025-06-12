* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.Apply.html

#  [MaterialPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.html).Apply
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
public void Apply([MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) prop); 
### Parameters
Parameter | Description  
---|---  
prop | The [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) to apply values for.  
### Description
Apply extra initial values to the material.
This function is called in all property drawers when a new material is created, or a shader is changed on an existing material. This lets the property drawers apply any extra values to the materials, for example to setup shader keywords.  
  
Note that if you change a property by assigning a value to it, Apply() is not called automatically. If you have any extra setup you need it to do, you should call it yourself.
* * *
