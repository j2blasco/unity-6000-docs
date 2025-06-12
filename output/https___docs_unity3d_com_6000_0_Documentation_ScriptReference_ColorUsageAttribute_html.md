* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUsageAttribute.html

# ColorUsageAttribute
class in UnityEngine
/
Inherits from:[PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Attribute used to configure the usage of the ColorField and Color Picker for a color.
Use this attribute on a Color to configure the Color Field and Color Picker to show/hide the alpha value and whether to treat the color as a HDR color or as a normal LDR color.
### Properties
Property | Description  
---|---  
[hdr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUsageAttribute-hdr.html) | If set to true the Color is treated as a HDR color.  
[showAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUsageAttribute-showAlpha.html) | If false then the alpha bar is hidden in the ColorField and the alpha value is not shown in the Color Picker.  
### Constructors
Constructor | Description  
---|---  
[ColorUsageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUsageAttribute-ctor.html) | Attribute for Color fields. Used for configuring the GUI for the color.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
