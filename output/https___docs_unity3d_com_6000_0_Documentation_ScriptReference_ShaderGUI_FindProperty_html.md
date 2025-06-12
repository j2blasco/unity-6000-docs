* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.FindProperty.html

#  [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).FindProperty
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
protected static [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) FindProperty(string propertyName, MaterialProperty[] properties); 
## Declaration
protected static [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) FindProperty(string propertyName, MaterialProperty[] properties, bool propertyIsMandatory); 
### Parameters
Parameter | Description  
---|---  
propertyName | The name of the material property.  
properties | The array of available material properties.  
propertyIsMandatory | If true then this method will throw an exception if a property with propertyName was not found.  
### Returns
**MaterialProperty** The material property found, otherwise null. 
### Description
Find shader properties.
This is a utility method that finds a MaterialProperty by name.
* * *
